import sqlite3
from datetime import datetime
from pathlib import Path

import pandas as pd

from expense_tracker.security.auth import hash_password, secure_compare

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "expenses.db"


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute(
        """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL
        )"""
    )
    conn.execute(
        """CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            amount REAL NOT NULL,
            type TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            created_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )"""
    )
    return conn


def register_user(username: str, password: str) -> bool:
    if not username.strip() or len(password) < 6:
        return False
    conn = get_conn()
    try:
        conn.execute(
            "INSERT INTO users (username, password_hash, created_at) VALUES (?, ?, ?)",
            (username.strip(), hash_password(password), datetime.utcnow().isoformat()),
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def authenticate_user(username: str, password: str):
    conn = get_conn()
    row = conn.execute("SELECT id, username, password_hash FROM users WHERE username = ?", (username.strip(),)).fetchone()
    conn.close()
    if not row:
        return None
    if secure_compare(row[2], hash_password(password)):
        return row[0], row[1]
    return None


def insert_transaction(user_id: int, tx: dict):
    conn = get_conn()
    conn.execute(
        "INSERT INTO transactions (user_id, date, amount, type, category, description, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (user_id, tx["date"], float(tx["amount"]), tx["type"], tx["category"], tx.get("description", ""), datetime.utcnow().isoformat()),
    )
    conn.commit()
    conn.close()


def load_transactions(user_id: int):
    conn = get_conn()
    df = pd.read_sql_query(
        "SELECT id, date, amount, type, category, description, created_at FROM transactions WHERE user_id = ? ORDER BY date DESC, id DESC",
        conn,
        params=(user_id,),
    )
    conn.close()
    return df
