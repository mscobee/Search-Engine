from nltk.stem import PorterStemmer
from urllib.request import urlopen
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
class HtmlCleaner:


    def __init__(self) -> None:
        self.ps = PorterStemmer()
        self.stop_words = set(stopwords.words('english'))

        
    def remove_stop_words(self):
        new_text = ''
        for w in self.content:
            if w not in self.stop_words:
                new_text += w + ' '
            self.set_data(new_text) # this is shit i think? find more efficient way to do the data transfers
    def stemming(self):
        new_text = ''
        for word in self.content:
            new_text += (self.ps.stem(word) + ' ')
        self.content = new_text

    def set_data(self, content):
        # split the string content into a list on all whitespace and '|'
        self.content = re.split('\||\s', content)
    def run_clean(self):
        self.content = self.__stemming()
        return self.content
    


    