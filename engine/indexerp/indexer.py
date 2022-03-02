import databasep, os
from pathlib import Path
class Indexer:
    def __init__(self) -> None:
        self.new_file = None
        self.dbc = databasep.DatabaseController(
            '/home/michael/dev/search-engine/engine/indexerp/html_files'
        )
        self.dir_path = self.dbc.save_dir
        self.file_name = None


    def set_database(self):
        self.dbc.connect_database()
        self.dbc.set_cursor()


    def set_data(self, title):
        self.title = title
        self.file_name = title + '.html'
        self.dbc.set_title('test')
        self.abs_path = os.path.join(self.dir_path, self.file_name)

    def insert(self):
        self.dbc.insert_data()


    def create_file(self, content):
        self.new_file = Path(self.abs_path)
        self.new_file.touch(exist_ok=True)
        self.new_file = open(self.abs_path, 'wb')
        self.new_file.write(content)
        self.new_file.close()

    