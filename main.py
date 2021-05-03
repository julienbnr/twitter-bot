from client import twitter_client
from config import get_twitter_credentials, get_search_config
from queries import search
from util import get_string_user_accounts

# import config
print("Get the twitter credentials from config file...")
search_config = get_search_config()
twitter_credentials = get_twitter_credentials()

# get the twitter client api
print("Get the twitter client with credentials from config...")
api = twitter_client(twitter_credentials)

# perform search
print("Perform search query on Twitter...")
user_accounts = search(api, search_config)

# printing results
if 0 == len(user_accounts):
    print("No user account found.")
else:
    print(str(len(user_accounts)) + " user(s) account(s) found.")
    print(get_string_user_accounts(user_accounts))
