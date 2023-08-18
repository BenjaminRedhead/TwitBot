import requests
from bs4 import BeautifulSoup

#TODO: refactor code into a class

class Webscraper:
    def __init__(self) -> None:
        pass

    def getData(self):
        pass

def scrape_bbc_headlines():
    """
    Returns a dict, indexed by headline, of urls to various articles on the bbc website
    TODO: get the article text from an article on the bbc website.
    """
    page = requests.get("https://www.bbc.com/news")
    soup = BeautifulSoup(page.content, "html.parser")
    headlines_dict = {}
    for a in soup.find_all("a", class_="gs-c-promo-heading"):
        headline = a.find_next('h3')
        if headline not in headlines_dict:
            hyperlink = a["href"]
            if hyperlink[0] == "/":
                hyperlink = "https://www.bbc.com" + hyperlink

            headlines_dict[headline.text] = a["href"]
    return headlines_dict

def scrape_bbc_article(url):
    page = requests.get(url)
    

headlines = scrape_bbc_headlines()
for i in headlines:
    print(f"{i}: {headlines[i]}")

