from tokenize import String
from urllib.request import urlopen
from bs4 import BeautifulSoup
from .my_queue import My_Queue
from nltk.stem import *
class Crawler:
    """Crawler is an object that can be used to Crawl web pages and store their content using BeautifulSoup4"""

    def __init__(self) -> None:
            self.href_queue = My_Queue()


    def crawl(self, indexer, webpage):
        self.add_hrefs_queue(webpage.get_soup())
        # self.print_queue()
        indexer.set_database()
        indexer.set_data(webpage.get_title())
        indexer.insert()
        indexer.create_file(webpage.get_content())


    def get_queue(self) -> My_Queue:
        return self.href_queue


    def add_hrefs_queue(self, soup) -> None:
        """Adds all of the href nodes of the current web page to the queue."""
        href_list = soup.find_all('a')
        for link in href_list:
            href_data = link.get('href')
            if href_data is None or href_data is '':
                continue
            if href_data.startswith('http'):
                url = href_data
            else:
                url = 'https:' + href_data
            self.href_queue.push(url)


    def print_queue(self):
        print(self.href_queue.get_queue())
  
 
    




