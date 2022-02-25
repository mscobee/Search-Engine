from crawler import Crawler

def main():
    """Main function driver"""
    crawler = Crawler()
    # Initial URL that the crawler begins from
    initial_url = 'https://www.wikipedia.org/'
    # store the web page based on the url
    crawler.set_page(initial_url)
    crawler.set_soup()
    crawler.add_hrefs_queue()
    crawler.print_queue()

    

if __name__ == "__main__":
    main()