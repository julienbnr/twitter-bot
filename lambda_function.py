from queries import search, display
from client import twitter_client
from mail import send_email

# lambda entry point function
def lambda_handler(event, context):
    api = twitter_client()
    user_tweets = search(api)

    if 0 == len(user_tweets):
        print("No tweet found.")
    else:
        print(str(len(user_tweets)) + " Users tweet found.")
        body = display(user_tweets)
        send_email("Potential YieldFarming x100", body, "")
