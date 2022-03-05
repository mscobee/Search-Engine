from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
class WebPage:
    def __init__(self) -> None:
        # headers required to avoid server rejection
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
        Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}


    def set_page_data(self,url):
        self.__set_url(url)
        self.__set_connection()
        self.__set_title()
        self.__set_soup()
        self.__set_content()

    def __set_url(self,url):
        self.url = url


    def get_url(self) -> str:
        return self.url

    def __set_title(self):
        self.title = BeautifulSoup(urlopen(self.url), features='lxml').title.get_text()
    
    def get_title(self) -> str:
        return self.title
    
    
    def __set_connection(self):
        try:
            page = requests.get(self.url, headers = self.headers)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        self.page = page
    
    def __set_soup(self) -> None:
        """Sets the soup variable to a BeautifulSoup object created with the current web page"""
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

    def get_soup(self) -> BeautifulSoup:
        return self.soup


    def __set_content(self):
        self.page_content = self.soup.get_text('|', strip=True)
        
    
    def get_content(self):
        return self.page_content
    