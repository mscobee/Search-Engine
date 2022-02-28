import os
import my_db
# 
class Indexer:
    def __init__(self) -> None:
        self.new_file = None
        self.dbc = my_db.Database_Controller(
            my_db.dbi.login,
            my_db.dbi.pw,
            my_db.dbi.host,
            my_db.dbi.port,
            my_db.dbi.db,
            '/home/michael/dev/search-engine/engine/indexer/html_files'
        )
        self.dir_path = self.dbc.save_dir
        self.file_name = None


    def set_database(self):
        self.dbc.connect_database()
        self.dbc.set_cursor()


    def set_data(self, title):
        self.file_name = title + '.html'
        self.dbc.set_title(title)
        self.abs_path = os.path.join(self.dir_path, self.file_name)

    def insert(self):
        self.dbc.insert_data()


    def create_file(self, content):
        self.new_file = open(self.abs_path, 'w')
        self.new_file.write(content)
        self.new_file.close()

    