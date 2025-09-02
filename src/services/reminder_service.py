import threading
import time
from datetime import datetime, timezone
import asyncio
from src.database.db import get_conn
from src.utils.logger import logging

logger = logging.getLogger(__name__)


def add_reminder(chat_id: int, message: str, remind_at: datetime) -> str:
    """
    Add a reminder row to the DB.
    'remind_at' MUST be timezone-aware (UTC).
    """
    if remind_at.tzinfo is None:
        raise ValueError("remind_at must be timezone-aware (UTC)")

    try:
        logger.info(f"Adding reminder for chat_id={chat_id} at {remind_at.isoformat()}")
        with get_conn() as (conn, cur):
            cur.execute(
                "INSERT INTO reminders (chat_id, message, remind_at) VALUES (%s, %s, %s)",
                (chat_id, message, remind_at)
            )
            conn.commit()

        return f"✅ Reminder set for {remind_at.isoformat()}: {message}"

    except Exception as e:
        logger.error(f"Failed to add reminder for chat_id={chat_id}: {e}")
        return f"❌ Failed to set reminder: {str(e)}"


def check_reminders(bot, loop):
    """
    Background poller: sends due reminders, marks them inactive.
    Runs forever in a thread with retries.
    """
    while True:
        try:
            with get_conn() as (conn, cur):
                now = datetime.now(timezone.utc)
                cur.execute(
                    "SELECT id, chat_id, message FROM reminders WHERE remind_at <= %s AND is_active=TRUE",
                    (now,)
                )
                reminders = cur.fetchall()

                for row in reminders:
                    try:
                        reminder_id = row["id"]
                        chat_id = row["chat_id"]
                        message_text = row["message"]

                        logger.info(f"Sending reminder to chat_id={chat_id}: {message_text}")

                        # ✅ Schedule send_message back on main event loop
                        asyncio.run_coroutine_threadsafe(
                            bot.send_message(chat_id, f"⏰ Reminder: {message_text}"),
                            loop
                        )

                        cur.execute("UPDATE reminders SET is_active=FALSE WHERE id=%s", (reminder_id,))
                    except Exception as inner_e:
                        logger.error(f"Error processing reminder {row}: {inner_e}")

                conn.commit()

            time.sleep(5)

        except Exception as e:
            logger.error(f"Error in check_reminders loop: {e}")
            time.sleep(60)  # Cool-off before retrying


def start_reminder_thread(bot, loop):
    """
    Start the reminder background thread.
    """
    try:
        logger.info("Starting reminder background thread...")
        thread = threading.Thread(target=check_reminders, args=(bot, loop), daemon=True)
        thread.start()
    except Exception as e:
        logger.error(f"Failed to start reminder thread: {e}")
