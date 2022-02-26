from queue import SimpleQueue
import time
from tokenize import String
from urllib import response
from lxml import html
from bs4 import BeautifulSoup
from my_queue import My_Queue
import requests
class Crawler:
    

    def __init__(self) -> None:
            # headers required to avoid server rejection
            self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
            self.soup = None
            self.page = None
            self.href_queue = My_Queue()

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

    # some of the hrefs have a schema and some do not 
    # TODO fix the above and check if schema needs to be applied before adding to queue? Will slow down function however.
    # because the urls that do possess scehmas are all at the end of bs4.element.Tag object could I iterate from the end and check for
    # the schema on each url and once one an instance without one occurs the logical check can stop?
    # TODO how to start at the end of the bs4.element.Tag?
    def add_hrefs_queue(self) -> None:
        """Adds all of the href nodes of the current web page to the queue."""
        for href in self.soup.findAll('a'):
            print(type(href))
            time.sleep(60)
            url = 'https:' + href.get('href')
            self.href_queue.push(url)
    
    def print(self):
        print(self.href_queue.get_queue())
  
 
    




