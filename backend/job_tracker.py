# backend/job_tracker.py

import sqlite3
from datetime import datetime

DB_PATH = "data/database.db"

def init_db():
    """
    Create the jobs table if it doesn't exist.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT NOT NULL,
        role TEXT NOT NULL,
        applied_date TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def add_job(company, role, status="Applied"):
    """
    Add a new job application.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO jobs (company, role, applied_date, status)
    VALUES (?, ?, ?, ?)
    """, (company, role, datetime.today().strftime("%Y-%m-%d"), status))

    conn.commit()
    conn.close()


def update_status(job_id, new_status):
    """
    Update job application status.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE jobs
    SET status = ?
    WHERE id = ?
    """, (new_status, job_id))

    conn.commit()
    conn.close()


def get_all_jobs():
    """
    Return all job applications.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()

    conn.close()
    return rows


def get_jobs_by_status(status):
    """
    Fetch only jobs matching a specific status.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM jobs WHERE status = ?", (status,))
    rows = cursor.fetchall()

    conn.close()
    return rows