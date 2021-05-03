from user_tweet import UserTweet
from util import get_filtered_usernames_by_tweet_list, is_user_eligible_for_retrieving, str_list_to_join_string

# retrieve the last nb tweets of specified user
def get_user_timelines(api, user_name, max_retrieve_nb_tweet):
    return api.user_timeline(
        screen_name=user_name,
        count=max_retrieve_nb_tweet, # should be inferior than 100
        include_rts = False,
        tweet_mode = 'extended'
    )

def get_user_account_from_user_timelines(timelines, screen_name, config_keywords):
    url = ''
    last_tweet = ''
    tweet_keywords = []

    if len(timelines) > 0:
        tweet = timelines[0]
        last_tweet = tweet.full_text
        if tweet.user.url:
            url = tweet.user.url
        for tweet_timeline in timelines:
            current_tweet = tweet_timeline.full_text.lower()
            for keyword in config_keywords:
                if keyword in current_tweet and keyword not in tweet_keywords:
                    tweet_keywords.append(keyword)
    return UserTweet(screen_name, last_tweet, tweet_keywords, url)

# search tweets on twitter
def search(api, search_config):

    # retrieve config
    print("Retrieving search configuration...")
    query = search_config['search']['query']
    order = search_config['search']['order']
    max_result = search_config['search']['count']
    max_user_tweet_timeline = search_config['search']['max_user_tweet_timeline']
    user_name_keywords = search_config['user_name_keywords']
    tweet_keywords = search_config['tweet_keywords']

    # perform search of last n tweets
    print("Searching " + query + " in mode " + order + " for the last " + str(max_result) + " results...")
    tweets = api.search(q=query, result_type=order, count=max_result)
    print(str(len(tweets)) + " result(s) found !")

    # apply filter on username
    print("Applying filter on username. Username must include one of these [" + str_list_to_join_string(user_name_keywords) + "]")
    user_names = get_filtered_usernames_by_tweet_list(tweets, user_name_keywords)
    print(str(len(user_names)) + " user(s) account(s) with one of these keywords in username found")

    user_accounts = []
    for user_name in user_names:
        print(user_name)
        user_timeline = get_user_timelines(api, user_name, 10)
        if is_user_eligible_for_retrieving(user_timeline, max_user_tweet_timeline):
            user_account = get_user_account_from_user_timelines(user_timeline, user_name, tweet_keywords)
            user_accounts.append(user_account)
    print("Finding " + str(len(user_accounts)) + " eligible user(s) account(s) during search...")
    return user_accounts
