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
    cleaner.set_data(webpage.get_content())
    print('Before')
    print(cleaner.content)

    print('After stopword removal')
    cleaner.remove_stop_words()
    print(cleaner.content)

    print('after stemming')
    cleaner.stemming()
    print(cleaner.content)
    

if __name__ == "__main__":
    main()