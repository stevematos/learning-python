import requests
from bs4 import BeautifulSoup

URL = "https://www.gob.pe"
page = requests.get(URL)
# print(page.text)


soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(attrs={"aria-labelledby": "estado-peruano-label"})
entities_peruvian = results.find_all("div", class_="power-home__title")

for entity in entities_peruvian:
    print(entity.text)
