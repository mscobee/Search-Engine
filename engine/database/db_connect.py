# Module Imports
import mariadb
import sys
import db_info
class Database_Controller:
    def __init__(self, login, pw, host, port, db, save_directory) -> None:
        self.login = login
        self.pw = pw
        self.host = host
        self.port = port
        self.db = db
        self.save_dir = save_directory
        self.conn = None
        self.cur = None
        self.index_title = None

    # def set_path(self):
    #     self.index_path = self.save_dir + '/' + self.index_title + '.html'()

    def connect_database(self):
        try:
            self.conn = mariadb.connect(user=self.login,
            password=self.pw,
            host=self.host,
            port=self.port,
            database=self.db)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

    def set_cursor(self):
        self.cur = self.conn.cursor()

    def set_title(self, title):
        self.index_title = title

    def insert_data(self):
        self.cur.execute(
    "INSERT INTO websites (title,content) VALUES \
        (?, ?)", (self.index_title,self.save_dir + '/' + self.index_title + '.html'))
        self.conn.commit()

# Get Cursor
# cur = conn.cursor()

# title = 'Google'
# content = 'A website search engine.'
# cur.execute(
#     "INSERT INTO websites (title,content) VALUES (?, ?)", 
#     (title,content))
# conn.commit()