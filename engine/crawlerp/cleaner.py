from nltk.stem import *
from nltk.stem.porter import *
class HtmlCleaner:
    def __init__(self) -> None:
        stemmer = PorterStemmer()