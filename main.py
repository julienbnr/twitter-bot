import json

from queries import search, display
from client import twitter_client

with open('json/config.json') as config_json:
    config = json.load(config_json)

    api = twitter_client(config)
    user_tweets = search(api)

    if 0 == len(user_tweets):
        print("No tweet found.")
    else:
        print(str(len(user_tweets)) + " Users tweet found.")
        display(user_tweets)

