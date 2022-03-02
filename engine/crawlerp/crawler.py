from tokenize import String
from lxml import html
from bs4 import BeautifulSoup
from .my_queue import My_Queue
import requests
class Crawler:
    """Crawler is an object that can be used to Crawl web pages and store their content using BeautifulSoup4"""

    def __init__(self) -> None:
            # headers required to avoid server rejection
            self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
            self.soup = None
            self.page = None
            self.href_queue = My_Queue()


    def get_queue(self) -> My_Queue:
        return self.href_queue


    def set_page(self, url) -> None:
        """Attempts to establish a connection to the given url using requests and return the response object"""
        try:
            page = requests.get(url, headers = self.headers) # Headers needed by the crawler to avoid a server rejecting access
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        self.page = page
    

    def set_soup(self) -> None:
        """Sets the soup variable to a BeautifulSoup object created with the current web page"""
        self.soup = BeautifulSoup(self.page.content, 'lxml')


    def get_content(self):
        return self.page.content

    def add_hrefs_queue(self) -> None:
        """Adds all of the href nodes of the current web page to the queue."""
        href_list = self.soup.find_all('a')
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
  
 
    




