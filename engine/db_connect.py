# Module Imports
import mariadb
import sys
import db_info

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user=db_info.login,
        password=db_info.pw,
        host=db_info.host,
        port=db_info.port,
        database=db_info.db
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

title = 'Google'
content = 'A website search engine.'
cur.execute(
    "INSERT INTO websites (title,content) VALUES (?, ?)", 
    (title,content))
conn.commit()