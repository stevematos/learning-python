import requests

URL = "https://www.amazon.com"
page = requests.get(URL)
print(page.text)
