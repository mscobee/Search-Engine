import crawlerp
import indexerp
import re
def main():
    """Main function driver"""
    # initial_url = 'http://localhost:8080/'
    webpage = crawlerp.WebPage()
    crawler = crawlerp.Crawler()
    indexer = indexerp.Indexer()
    cleaner = crawlerp.HtmlCleaner()
    # url_queue = crawler.get_queue()
    webpage.set_page_data('https://www.github.com/')
    cleaner.set_data(re.split('\||\s', webpage.get_content()))
    cleaner.run_clean()
    webpage.set_content(cleaner.get_cleaned())
    # crawler.crawl(indexer, webpage)
    print(webpage.get_title())
    print(webpage.get_content())

    # while url_queue:
    #     webpage.set_page_data(url_queue.pop())
    #     cleaner.set_data(re.split('\||\s', webpage.get_content()))
    #     cleaner.run_clean()
    #     webpage.set_content(cleaner.get_cleaned())
    #     crawler.crawl(indexer, webpage)
    #     url_queue.print()

if __name__ == "__main__":
    main()