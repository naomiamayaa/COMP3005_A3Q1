import os
import psycopg
from datetime import date
from dotenv import load_dotenv 

load_dotenv() # Load environment variables from .env file

def get_conn():
    return psycopg.connect(
        host=os.getenv("PGHOST", "localhost"),
        port=os.getenv("PGPORT", "5432"),
        dbname=os.getenv("PGDATABASE", "comp3005"),
        user=os.getenv("PGUSER", "postgres"),
        password=os.getenv("PGPASSWORD", "")
    )

# Retrieves and displays all records from the students table.
def getAllStudents():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT student_id, first_name, last_name, email, enrollment_date FROM students ORDER BY student_id;")
        rows = cur.fetchall()
        for r in rows:
            print(r)

# Inserts a new student record into the students table.
def addStudent(first_name, last_name, email, enrollment_date):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
            (first_name, last_name, email, enrollment_date)
        )
        new_id = cur.fetchone()[0]
        print(f"Inserted student_id={new_id}")

# Updates the email address for a student with the specified student_id.
def updateStudentEmail(student_id, new_email):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            "UPDATE students SET email = %s WHERE student_id = %s;",
            (new_email, student_id)
        )
        print(f"Updated student_id={student_id} with new email={new_email}")

# Deletes the record of the student with the specified student_id.
def deletStudent(student_id): 
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            "DELETE FROM students WHERE student_id = %s;",
            (student_id,)
        )
        print(f"Deleted student_id={student_id}")
    
if __name__ == "__main__":
    print("All Students:")
    getAllStudents()