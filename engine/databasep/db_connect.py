# Module Imports
import mariadb
import sys
import databasep.db_info as dbi
class DatabaseController:
    """Database Controller is used to connect to a databased and can be used to insert data"""
    # TODO add database removal
    def __init__(self, save_directory) -> None:
        self.login = dbi.login
        self.pw = dbi.pw
        self.host = dbi.host
        self.port = dbi.port
        self.db = dbi.db
        self.save_dir = save_directory
        self.conn = None
        self.cur = None
        self.index_title = None

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
