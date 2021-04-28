from queries import search, display
from client import twitter_client

api = twitter_client()
user_tweets = search(api)

if 0 == len(user_tweets):
    print("No tweet found.")
else:
    print(str(len(user_tweets)) + " Users tweet found.")
    display(user_tweets)
