import tweepy

# authenticate to twitter
def twitter_client(config):
    auth = tweepy.OAuthHandler(config['twitter']['api_key'], config['twitter']['api_secret_key'])
    auth.set_access_token(config['twitter']['access_token'],  config['twitter']['access_token_secret'])
    return tweepy.API(auth)
