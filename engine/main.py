from imp import init_builtin
import crawlerp
import indexerp
import re
def main():
    """Main function driver"""
    initial_url = 'https://www.wikipedia.com/'
    webpage = crawlerp.WebPage()
    crawler = crawlerp.Crawler()
    indexer = indexerp.Indexer()

    webpage.set_page_data(initial_url)
    crawler.crawl(indexer, webpage)
    

if __name__ == "__main__":
    main()