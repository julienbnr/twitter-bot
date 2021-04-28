import json

from queries import search, display
from client import twitter_client

with open('json/config.json') as search_json:
    config = json.load(search_json)

    api_key = config['twitter']['api_key']
    api_secret_key = config['twitter']['api_secret_key']
    access_token = config['twitter']['access_token']
    access_token_secret = config['twitter']['access_token_secret']

    api = twitter_client(api_key, api_secret_key, access_token, access_token_secret)
    user_tweets = search(api)

    if 0 == len(user_tweets):
        print("No tweet found.")
    else:
        print(str(len(user_tweets)) + " Users tweet found.")
        display(user_tweets)
