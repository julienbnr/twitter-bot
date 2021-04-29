import boto3

# send an email to sns subscribers
def send_email(subject, message, topic_arn):
    print('sending email to subscribers...')
    client = boto3.client('sns')
    response = client.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject=subject
    )
    print('sending email to sns subscribers complete.')

def get_message_body(user_tweets):
    body = ""
    for user_tweet in user_tweets:
        body = body + "User = " + user_tweet.user_name + "\n"
        body = body + "Profile link = https://twitter.com/" + user_tweet.user_name + "\n"
        body = body + "Last Tweet = " + user_tweet.last_tweet + "\n"
        body = body + "Keywords of last 10 tweets = " + get_concat_keyword(user_tweet.keywords) + "\n"
        body = body + "\n"
    return body

def get_concat_keyword(keywords):
    concat_keyword = ""
    for keyword in keywords:
        concat_keyword = concat_keyword + keyword + " / "
    return concat_keyword
