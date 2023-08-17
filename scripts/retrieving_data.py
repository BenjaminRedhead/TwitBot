import requests
from bs4 import BeautifulSoup
class Webscraper:
    def __init__(self) -> None:
        pass

    def getData(self):
        pass

def scrape_bbc_headlines():
    """
    Returns a list of headlines from the bbc news main page
    """
    page = requests.get("https://www.bbc.com/news")
    soup = BeautifulSoup(page.content, "html.parser")
    headlines = soup.find_all("h3", class_="gs-c-promo-heading__title")
    return headlines

for headline in scrape_bbc_headlines():
    print(headline.text)


