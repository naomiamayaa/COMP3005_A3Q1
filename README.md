## COMP3005_A3Q1
Implemented a PostgreSQL database using the 'Student' entity and wrote a python application that connects to this database to perform specific CRUD (Create, Read, Update, Delete) operations..

## Author
Authored by Naomi Amaya Lovett

## Instructions to build (if any)
# Prerequisites
* PostgreSQL 12+ installed (pgAdmin optional)
* Python 3.10+ installed
* Git installed
* macOS/Windows/Linux supported

1. Clone the repo:
    git clone <YOUR_REPO_URL> comp3005_a3q1
    cd comp3005_A3Q1

2. Create venv
    MacOS / Linux: 
        python3 -m venv venv
        source venv/bin/activate

    Windows:
        python -m venv venv
        venv\Scripts\activate

3. Install Python dependencies
    pip install -r requirements.txt

4. Create PostgreSQL DB
    create a fresh DB named comp3005
    psql -h localhost -U postgres
    CREATE DATABASE comp3005;
    \c comp3005
    \q

5. Create a .env file in the project root (same folder as README.md):
    PGHOST=localhost
    PGPORT=5432
    PGDATABASE=comp3005
    PGUSER=postgres
    PGPASSWORD=<YOUR_PASSWORD>

6. Initialize schema 
    psql -h localhost -U postgres -d comp3005 -f db/init.sql

## Instructions to run
    python app/main.py
