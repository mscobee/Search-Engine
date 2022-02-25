from crawler import Crawler

def main():
    """Main function driver"""
    crawler = Crawler()
    # Initial URL that the crawler begins from
    initial_url = 'https://www.wikipedia.org/'
    # store the web page based on the url
    crawler.run_scrape(initial_url)

    

if __name__ == "__main__":
    main()