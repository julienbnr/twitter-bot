import tweepy

# authenticate to twitter
def twitter_client(config):
    auth = tweepy.OAuthHandler(config['api_key'], config['api_secret_key'])
    auth.set_access_token(config['access_token'],  config['access_token_secret'])
    return tweepy.API(auth)
