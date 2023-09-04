import requests
from bs4 import BeautifulSoup
from posting import Twitter

#TODO: Attach an SQL database to this to record historical news

class Webscraper:
    def __init__(self) -> None:
        pass

    def getData(self):
        pass

class BBC_scraper:
    """
    A class containing the latest headlines from the BBC news website at the point of initialisation.
    """
    def __init__(self) -> None:
        self.headlines = self.scrape_bbc_headlines()
    
    def __getitem__(self, key):
        return self.scrape_bbc_article(self.headlines(key))
    
    def get_headlines(self):
        return list(self.headlines.keys())


    def scrape_bbc_headlines(self):
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

    def scrape_bbc_article(self, url):
        """
        Takes a URL to a bbc news article as an argument and returns the article text.
        """
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        paragraphs = soup.find_all("p", class_="ssrcss-1q0x1qg-Paragraph e1jhz7w10")
        article_text = ""
        for p in paragraphs:
            article_text += p.text + "\n"
        return article_text

scraper = BBC_scraper()
latest_headline = scraper.get_headlines()[0]

bot = Twitter()
bot.post(latest_headline)






