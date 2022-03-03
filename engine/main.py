import crawlerp
import indexerp
import re
def main():
    """Main function driver"""
    crawler = crawlerp.Crawler()
    indexer = indexerp.Indexer()
    link_queue = crawler.get_queue()
    initial_url = 'https://www.wikipedia.com/'
    crawler.crawl(initial_url)
    


if __name__ == "__main__":
    main()