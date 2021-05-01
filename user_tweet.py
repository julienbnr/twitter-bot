def get_concat_keyword(keywords):
    separator = '/'
    return separator.join(keywords)


def display_all(user_tweets):
    for user_tweet in user_tweets:
        display(user_tweet)
        print("\n")

def display(user_tweet):
    print("Username=" + user_tweet.user_name)
    print("LastTweet=" + user_tweet.last_tweet)
    print("Keywords=" + get_concat_keyword(user_tweet.keywords))

class UserTweet:

    def __init__(self, user_name, last_tweet, keywords):
        self.user_name = user_name
        self.last_tweet = last_tweet
        self.keywords = keywords
