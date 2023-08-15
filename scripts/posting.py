import tweepy
from KEYS import KEY, SECRET_KEY, TOKEN, SECRET_TOKEN

class Twitter:
    """
    This class is an interface for posting with the twitter API
    """
    def __init__(self) -> None:
        """
        Initialises and stores the v2 api client and the v1.1 api
        """
        self.client = tweepy.Client(
            consumer_key=KEY,
            consumer_secret=SECRET_KEY,
            access_token=TOKEN,
            access_token_secret=SECRET_TOKEN
        )
        auth = tweepy.OAuth1UserHandler(KEY, SECRET_KEY)
        auth.set_access_token(TOKEN, SECRET_TOKEN)
        self.api = tweepy.API(auth)
    
    def post(self, text):
        """
        Posts a tweet with the given text
        """
        self.client.create_tweet(text=text)

"""acc = Twitter()
acc.post("testing nonpicture tweet")"""