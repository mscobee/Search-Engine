from tokenize import String
from urllib import response
from lxml import html
from bs4 import BeautifulSoup
import requests
class Crawler:
    

    def __init__(self) -> None:
            # headers required to avoid server rejection
            self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
            self.soup = None
            self.page = None
            self.href_queue = []

    def set_page(self, url):
        """Attempts to establish a connection to the given url using requests and return the response object"""
        try:
            page = requests.get(url, headers = self.headers) # Headers needed by the crawler to avoid a server rejecting access
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        self.page = page
    
    def set_soup(self) -> None:
        """Sets the soup variable to a BeautifulSoup object created with the current web page"""
        self.soup = BeautifulSoup(self.page.content, 'lxml')

    def add_hrefs_queue(self) -> None:
        """Adds all of the href nodes of the current web page to the queue."""
        for href in self.soup.findAll('a'):
            self.href_queue.append(href.get('href'))
    
    def print_queue(self) -> None:
        print(self.href_queue)
    def run_scrape(self, url) -> None:
        self.set_page(url)
        self.set_soup()
        self.add_hrefs_queue()
        self.print_queue()
    def pop_queue(self) -> String:
        return self.href_queue.pop()




