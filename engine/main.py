import crawlerp
import indexerp

def main():
    """Main function driver"""
    crawler = crawlerp.Crawler()
    indexer = indexerp.Indexer()
    link_queue = crawler.get_queue()
    initial_url = 'http://localhost:8080/'
    crawler.crawl(initial_url, indexer)
    crawler.crawl(link_queue.pop(), indexer)
    crawler.crawl(link_queue.pop(), indexer)


if __name__ == "__main__":
    main()