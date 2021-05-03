import boto3

from user_tweet import get_concat_keyword
from datetime import datetime

DB_TABLE = 'twitter_accounts_bot'

# add an item in the table
def add_item(user_tweet):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(DB_TABLE)
    keywords = get_concat_keyword(user_tweet.keywords)
    table.put_item(
        Item = {
            'Username' : user_tweet.user_name,
            'LastTweet' : user_tweet.last_tweet,
            'Keywords' : keywords,
            'Date' : str(datetime.now()),
            'WebsiteUrl' : user_tweet.url
        }
    )

# check if db contains item
def has_item(username):
    client = boto3.client('dynamodb')
    response = client.query(
        TableName=DB_TABLE,
        KeyConditionExpression='Username = :username',
        ExpressionAttributeValues={
            ':username': {'S': username }
        }
    )
    return 0 < len(response['Items'])
