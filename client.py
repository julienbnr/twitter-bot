import json
import tweepy

# authenticate to twitter
def twitter_client(api_key, api_secret_key, access_token, access_token_secret):
    with open('json/config.json') as config_json:
        config = json.load(config_json)
        auth = tweepy.OAuthHandler(api_key, api_secret_key)
        auth.set_access_token(access_token, access_token_secret)
        return tweepy.API(auth)
