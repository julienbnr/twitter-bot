from client import twitter_client
from config import get_twitter_credentials, get_aws_config, get_search_config
from db import has_item, add_item
from queries import search
from util import get_string_user_accounts
from webhook import send_webhooks

# lambda entry point function
def lambda_handler(event, context):

    # import config
    config = get_aws_config()
    search_config = get_search_config()
    twitter_credentials = get_twitter_credentials()

    # get the twitter client api
    api = twitter_client(twitter_credentials)

    # perform queries for searching tweets...
    user_accounts = search(api, search_config)

    # getting not saved users accounts
    new_user_accounts = get_unregistered_user_accounts(config, user_accounts)

    if 0 == len(new_user_accounts):
        print("No unregistered user account.")
    else:
        print(str(len(new_user_accounts)) + " new user(s) account(s) found.")
        body = get_string_user_accounts(new_user_accounts)
        send_webhooks(config, user_accounts)
    return 0

# get unregistered user account
def get_unregistered_user_accounts(config, user_accounts):
    print("finding the not registered user(s) account(s) from result...")
    not_registered_user_accounts = []
    for user_account in user_accounts:
        username = user_account.user_name
        is_account_registered = has_item(config, username)
        if not is_account_registered:
            print(username + " is not registered")
            add_item(config, user_account)
            not_registered_user_accounts.append(user_account)
    print(str(len(not_registered_user_accounts)) + " not registered user(s) account(s) found...")
    return not_registered_user_accounts
