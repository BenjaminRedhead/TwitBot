import tweepy
from KEYS import KEY, SECRET_KEY, TOKEN, SECRET_TOKEN

client = tweepy.Client(
    consumer_key=KEY,
    consumer_secret=SECRET_KEY,
    access_token=TOKEN,
    access_token_secret=SECRET_TOKEN
)

auth = tweepy.OAuth1UserHandler(KEY, SECRET_KEY)
auth.set_access_token(TOKEN, SECRET_TOKEN)

api = tweepy.API(auth)

username = "FunctorFact"

user = api.get_user(screen_name=username)

