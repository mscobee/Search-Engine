from nltk.stem import PorterStemmer, WordNetLemmatizer
from urllib.request import urlopen
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import re
class HtmlCleaner:


    def __init__(self) -> None:
        self.__ps = PorterStemmer()
        self.__lemm = WordNetLemmatizer()
        self.__stop_words = set(stopwords.words('english'))

    def set_data(self, content):
        """accepts a list of strings"""
        # split the string content into a list on all whitespace and '|'
        # self.content = re.split('\||\s', content)
        self.content = content


    def __remove_stop_words(self):
        new_text = ''
        for w in self.content:
            if w not in self.__stop_words:
                new_text += w + ' '
            self.set_data(re.split('\||\s', new_text))
            
    def __stemming(self):
        new_text = ''
        for word in self.content:
            new_text += (self.__ps.stem(word) + ' ')
        # self.set_data(re.split('\||\s', new_text))
        self.content = new_text

    def __lemmatization(self):
        new_text = ''
        for word in self.content:
            new_text += self.__lemm.lemmatize(word) + ' '
        self.content = new_text

    def get_cleaned(self):
        return self.content

    def run_clean(self) -> None:
        self.__remove_stop_words()
        # print(self.content)
        self.__stemming()
        # print(self.content)
        # self.__lemmatization()
        # print(self.content)
    


    