import nltk
from urllib.request import urlopen
class HtmlCleaner:


    def __init__(self) -> None:
        pass

    def remove_html_tags(self, url) -> str:
        html = urlopen(url).read()
        return nltk.clean_html(html)
    


    
