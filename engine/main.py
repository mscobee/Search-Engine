import crawlerp
import indexerp
import re
def main():
    """Main function driver"""
    initial_url = 'https://tbc.wow-tools.com/tbc_arena_calculator'
    webpage = crawlerp.WebPage()
    crawler = crawlerp.Crawler()
    indexer = indexerp.Indexer()

    webpage.set_page_data(initial_url)
    crawler.crawl(indexer, webpage)
    crawler.print_queue()

if __name__ == "__main__":
    main()