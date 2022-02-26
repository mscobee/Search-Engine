from crawler import Crawler

def execute_crawling(crawler, url):
    crawler.set_page(url) 
    crawler.set_soup()
    crawler.add_hrefs_queue()
    crawler.print()
    print('NEW')


def main():
    """Main function driver"""
    crawler = Crawler()
    initial_url = 'https://www.wikipedia.org/'
    execute_crawling(crawler,initial_url)
    # print(len(crawler.href_queue.get_queue()))
    print(crawler.href_queue.pop())
    # execute_crawling(crawler,crawler.href_queue.pop())
    # print(len(crawler.href_queue.get_queue()))

    
    

if __name__ == "__main__":
    main()