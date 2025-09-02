from src.utils.logger import logging
from src.database.db import get_conn, get_server_conn, DB_CONFIG, init_pool

logger = logging.getLogger(__name__)

def create_database_if_not_exists():
    db_name = DB_CONFIG["database"]
    logger.info(f"Checking if database `{db_name}` exists...")
    with get_server_conn() as (conn, cur):
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        logger.info(f"✅ Database `{db_name}` is ready.")

def create_tables():
    logger.info("Creating required tables if not exist...")
    with get_conn() as (conn, cur):

        cur.execute("""
            CREATE TABLE IF NOT EXISTS user_conditions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                chat_id VARCHAR(64),
                user_condition VARCHAR(256),   -- ✅ renamed column
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        logger.debug("Table `user_conditions` checked/created.")

        cur.execute("""
            CREATE TABLE IF NOT EXISTS reminders (
                id INT AUTO_INCREMENT PRIMARY KEY,
                chat_id VARCHAR(64),
                message VARCHAR(512),
                remind_at DATETIME,
                repeat_cron VARCHAR(64),
                is_active BOOLEAN DEFAULT TRUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        logger.debug("Table `reminders` checked/created.")

        cur.execute("""
            CREATE TABLE IF NOT EXISTS symptom_logs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                chat_id VARCHAR(64),
                symptoms TEXT,
                possible_condition VARCHAR(256),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        logger.debug("Table `symptom_logs` checked/created.")

    logger.info("✅ All required tables initialized.")


def init_db():
    logger.info("Initializing database...")
    create_database_if_not_exists()
    init_pool()   #  Initialize pool AFTER DB is created
    create_tables()
    logger.info("✅ Database initialization complete.")
