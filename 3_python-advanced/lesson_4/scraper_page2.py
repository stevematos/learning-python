import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com"
page = requests.get(URL)
print(page.text)
