from pydoc import pager
from lxml import html
import requests

page_test = requests.get('https://recruitment.lazerhawks.net/')
html_test = html.fromstring(page_test.content)
