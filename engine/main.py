import crawlerp
import indexerp
# def execute_crawling(crawler, url, indexer):
#     print(f'Crawling URL: {url}')
#     crawler.set_page(url) 
#     crawler.set_soup()
#     crawler.add_hrefs_queue()
#     crawler.print_queue()
#     indexer.set_database()
#     print(f'PAGE TITLE:\t{crawler.get_page_title()}')
#     indexer.set_data(crawler.get_page_title())
#     indexer.insert()
#     indexer.create_file(crawler.get_content())

def main():
    """Main function driver"""
    crawler = crawlerp.Crawler()
    indexer = indexerp.Indexer()
    i = 0
    link_queue = crawler.get_queue()
    initial_url = 'http://localhost:8080/'
    crawler.crawl(initial_url, indexer)
    crawler.crawl(link_queue.pop(), indexer)
    crawler.crawl(link_queue.pop(), indexer)


if __name__ == "__main__":
    main()