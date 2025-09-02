import mysql.connector
from mysql.connector import pooling
from contextlib import contextmanager
import os
from dotenv import load_dotenv
from src.utils.logger import logging

load_dotenv()
logger = logging.getLogger(__name__)

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),  # Use IP, not "localhost"
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "medbot")
}

pool = None


# ✅ Server-level connection (no database selected)
@contextmanager
def get_server_conn():
    logger.debug("Establishing server-level connection (no DB selected)...")
    conn = mysql.connector.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )
    cursor = conn.cursor()
    try:
        yield conn, cursor
        conn.commit()
    except Exception as e:
        logger.error(f"Error in server-level connection: {e}")
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()
        logger.debug("Server-level connection closed.")


def init_pool():
    global pool
    try:
        pool = pooling.MySQLConnectionPool(
            pool_name="medbot_pool",
            pool_size=10,
            pool_reset_session=True,
            **DB_CONFIG
        )
        logger.info(
            f"MySQL connection pool created for DB `{DB_CONFIG['database']}` "
            f"at {DB_CONFIG['host']}:{DB_CONFIG['port']}."
        )
    except mysql.connector.Error as e:
        logger.error(f"Failed to create MySQL connection pool: {e}")
        pool = None


@contextmanager
def get_conn():
    if not pool:
        raise RuntimeError("MySQL connection pool not initialized. Did you call init_pool()?")

    logger.debug("Getting connection from pool...")
    conn = pool.get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        yield conn, cursor
        conn.commit()
        logger.debug("Transaction committed.")
    except Exception as e:
        conn.rollback()
        logger.error(f"Transaction rolled back due to error: {e}")
        raise
    finally:
        cursor.close()
        conn.close()
        logger.debug("Connection returned to pool.")
