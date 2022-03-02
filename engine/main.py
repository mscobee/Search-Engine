import crawlerp
import indexerp
def execute_crawling(crawler, url, indexer):
    print(f'Crawling URL: {url}')
    crawler.set_page(url) 
    crawler.set_soup()
    crawler.add_hrefs_queue()
    crawler.print_queue()
    indexer.set_database()
    print(f'PAGE TITLE:\t{crawler.get_page_title()}')
    indexer.set_data(crawler.get_page_title()) # currently set to url need to change to actual website name
    indexer.insert()
    indexer.create_file(crawler.get_content())

def main():
    """Main function driver"""
    crawler = crawlerp.Crawler()
    indexer = indexerp.Indexer()
    i = 0
    link_queue = crawler.get_queue()
    initial_url = 'http://localhost:8080/'
    execute_crawling(crawler,initial_url, indexer)
    execute_crawling(crawler, link_queue.pop(), indexer)
    execute_crawling(crawler, link_queue.pop(), indexer)


if __name__ == "__main__":
    main()