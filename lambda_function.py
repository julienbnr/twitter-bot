import json

from queries import search, display
from client import twitter_client
from mail import send_email, get_message_body
from db import has_item, add_item
from user_tweet import UserTweet, display_all

# lambda entry point function
def lambda_handler(event, context):
    with open('json/config.json') as config_json:
        config = json.load(config_json)

        api_key = config['twitter']['api_key']
        api_secret_key = config['twitter']['api_secret_key']
        access_token = config['twitter']['access_token']
        access_token_secret = config['twitter']['access_token_secret']
        topic_arn = config['sns']['topic_arn']

        api = twitter_client(api_key, api_secret_key, access_token, access_token_secret)
        potential_user_tweets = search(api)

        print("Finding " + str(len(potential_user_tweets)) + " potential tweets...")
        display_all(potential_user_tweets)

        user_tweet_email = []

        for tweet in potential_user_tweets:
            exist = has_item(tweet.user_name)
            if exist == False:
                add_item(tweet) # put new item
                user_tweet_email.append(tweet)

        if 0 == len(user_tweet_email):
            print("No new user tweet found.")
        else:
            print(str(len(user_tweet_email)) + " new users tweet found.")
            body = get_message_body(user_tweet_email)
            send_email("Potential YieldFarming x100", body, topic_arn)
        return 0
