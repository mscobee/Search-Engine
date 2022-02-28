from crawler import Crawler

def execute_crawling(crawler, url):
    print(f'Crawling URL: {url}')
    crawler.set_page(url) 
    crawler.set_soup()
    crawler.add_hrefs_queue()
    crawler.print_queue()

def main():
    """Main function driver"""
    crawler = Crawler()
    link_queue = crawler.get_queue()
    initial_url = 'http://localhost:8080/'
    # initial_url = 'https://www.geeksforgeeks.org/android-tutorial/'
    execute_crawling(crawler,initial_url)
    execute_crawling(crawler, link_queue.pop())


if __name__ == "__main__":
    main()