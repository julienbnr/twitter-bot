import json

from queries import search, display
from client import twitter_client
from mail import send_email, get_message_body

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
        user_tweets = search(api)

        if 0 == len(user_tweets):
            print("No tweet found.")
        else:
            print(str(len(user_tweets)) + " Users tweet found.")
            body = get_message_body(user_tweets)
        send_email("Potential YieldFarming x100", body, topic_arn)
        return 0
