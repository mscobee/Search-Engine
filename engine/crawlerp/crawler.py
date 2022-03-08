from tokenize import String
from urllib.parse import urlparse
from .my_queue import My_Queue
class Crawler:
    """Crawler is an object that can be used to Crawl web pages and store their content using BeautifulSoup4"""

    def __init__(self) -> None:
            self.href_queue = My_Queue()


    def crawl(self, indexer, webpage):
        self.add_hrefs_queue(webpage.get_soup())
        indexer.set_database()
        indexer.set_data(webpage.get_title())
        indexer.insert()
        indexer.create_file(webpage.get_content())


    def get_queue(self) -> My_Queue:
        return self.href_queue

    def validate_url(self, data):
        """validates that href data has both protocol and domain name"""
        url = urlparse(data)
        return bool(url.netloc) and bool(url.scheme)

    def add_hrefs_queue(self, soup) -> None:
        """Adds all of the href nodes of the current web page to the queue."""
        max_link_crawl = 5
        links_added = 0
        href_list = soup.find_all('a', href=True)
        for link in href_list:
            # return if 5 links have been added
            if links_added >= 5:
                return
            href_data = link.get('href')
            # check that data is a valid url before pushing to queue
            if not (self.validate_url(href_data)):
                continue
            else:
                self.href_queue.push(href_data)
                links_added += 1
            
            


    def print_queue(self):
        print(self.href_queue.get_queue())
  
 
    




