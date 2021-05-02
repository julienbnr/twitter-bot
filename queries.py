import tweepy
import json

from client import twitter_client
from user_tweet import UserTweet

def input_contains_elem_in_list(input, list):
    input = input.lower()
    for str in list:
        if str in input:
            return True
    return False

# filter tweets by user name contain
def filter_tweets(tweets, screen_name_must_contain):
    filtered_tweets = []
    for tweet in tweets:
        user_name = tweet.user.screen_name
        if (input_contains_elem_in_list(user_name, screen_name_must_contain)):
            filtered_tweets.append(tweet)
    return filtered_tweets

# get user tweets
def get_user_last_tweet(api, user_name, config_keywords):
    user_tweets = api.user_timeline(screen_name=user_name, count=10, include_rts = False, tweet_mode = 'extended')
    last_tweet = 'N/A'
    url = 'N/A'

    counter = 0
    tweet_keywords = []
    for tweet in user_tweets:
        if counter == 0:
            last_tweet = tweet.full_text
            if tweet.user.url:
                url = tweet.user.url
        current_tweet = tweet.full_text.lower()
        for keyword in config_keywords:
            if keyword in current_tweet and keyword not in tweet_keywords:
                tweet_keywords.append(keyword)
        counter = counter + 1
    return UserTweet(user_name, last_tweet, tweet_keywords, url)

# get user name list
def get_user_names(tweets):
    user_names = []
    for tweet in tweets:
        user_name = tweet.user.screen_name
        if user_name not in user_names:
            user_names.append(user_name)
    return user_names

# display user & tweet
def display(user_tweets):
    for user_tweet in user_tweets:
        concat_keyword = ""
        for keyword in user_tweet.keywords:
            concat_keyword = concat_keyword + keyword + " / "
        print("User = " + user_tweet.user_name)
        print("Profile link = https://twitter.com/" + user_tweet.user_name)
        print("URL = " + user_tweet.url)
        print("Last Tweet = " + user_tweet.last_tweet)
        print("Keywords of last 10 tweets = " + concat_keyword)
        print("\n")
    return concat_keyword

# search tweets on twitter
def search(api):
    with open('json/search.json') as search_json:
        search_config = json.load(search_json)
        query = search_config['query']
        user_name_keywords = search_config['user_name_keywords']
        tweet_keywords = search_config['tweet_keywords']
        tweets = api.search(q=query, result_type="recent", count=100)
        filtered_tweets = filter_tweets(tweets, user_name_keywords)
        user_names = get_user_names(filtered_tweets)

        user_tweets = []
        for user_name in user_names:
            user_tweet = get_user_last_tweet(api, user_name, tweet_keywords)
            user_tweets.append(user_tweet)
        return user_tweets
