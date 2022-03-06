import crawlerp
import indexerp
import re
def main():
    """Main function driver"""
    initial_url = 'http://localhost:8080/'
    webpage = crawlerp.WebPage()
    crawler = crawlerp.Crawler()
    indexer = indexerp.Indexer()
    cleaner = crawlerp.HtmlCleaner()

    webpage.set_page_data(initial_url)
    # crawler.crawl(indexer, webpage)
    cleaner.set_data(re.split('\||\s', webpage.get_content()))
    cleaner.run_clean()
    

if __name__ == "__main__":
    main()