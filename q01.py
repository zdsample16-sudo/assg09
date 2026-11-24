"""Question 01 Submission"""

import sqlite3


def setup_student_info_database(filename):
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Majors (
            MajorID INTEGER PRIMARY KEY,
            Name TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Departments (
            DeptID INTEGER PRIMARY KEY,
            Name TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            StudentID INTEGER PRIMARY KEY,
            Name TEXT,
            MajorID INTEGER,
            DeptID INTEGER,
            FOREIGN KEY (MajorID) REFERENCES Majors(MajorID),
            FOREIGN KEY (DeptID) REFERENCES Departments(DeptID)
        )
    """)

    conn.commit()
    conn.close()


def clear_student_info_database(filename):
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("DROP TABLE IF EXISTS Students")
    cursor.execute("DROP TABLE IF EXISTS Majors")
    cursor.execute("DROP TABLE IF EXISTS Departments")

    conn.commit()
    conn.close()

    setup_student_info_database(filename)
