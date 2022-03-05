import textwrap
import databasep, os
from pathlib import Path
class Indexer:
    """Indexer is used to index the web pages that the Crawler crawls"""
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
        """Set the title of the crawled web page, the file name that is to be saved and define the path of the file."""
        # self.title = title
        self.file_name = title + '.html'
        self.dbc.set_title(title)
        self.abs_path = os.path.join(self.dir_path, self.file_name)


    def insert(self):
        """Inserts the web page title and index location into the database."""
        self.dbc.insert_data()


    def create_file(self, content):
        """Creates a file in the target directory if it does not exist and writes the html content of the scraped
        website to the file."""
        self.new_file = Path(self.abs_path)
        self.new_file.touch(exist_ok=True)
        self.new_file = open(self.abs_path, 'w')
        self.new_file.write(textwrap.fill(content,width=75))
        self.new_file.close()

    