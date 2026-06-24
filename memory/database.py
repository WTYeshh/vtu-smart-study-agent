import sqlite3
import urllib.parse
from utils.config import Config
from utils.logger import setup_logger

logger = setup_logger("database")

def get_db_connection():
    """Establishes connection to the SQLite database based on Config.DATABASE_URL."""
    db_url = Config.DATABASE_URL
    if db_url.startswith("sqlite:///"):
        db_path = db_url.replace("sqlite:///", "")
    else:
        db_path = "vtu_study.db"
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the database schema if tables do not exist."""
    logger.info("Initializing SQLite Database...")
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create study plan table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS study_plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_code TEXT,
            subject_name TEXT,
            topic TEXT,
            module INTEGER,
            planned_date TEXT,
            status TEXT DEFAULT 'PENDING',
            completed_date TEXT
        )
    """)
    
    # Create quiz results table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_code TEXT,
            module INTEGER,
            score INTEGER,
            total_questions INTEGER,
            taken_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Create chat history/memory table for agents context
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT,
            role TEXT,
            message TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()
    logger.info("Database schema initialized successfully.")
