import boto3

from user_tweet import get_concat_keyword
from datetime import datetime

# add an item in the table
def add_item(config, user_tweet):
    dynamodb = boto3.resource('dynamodb')
    table_name = config['dynamo']['table_name']
    table = dynamodb.Table(table_name)
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
def has_item(config, username):
    client = boto3.client('dynamodb')
    table_name = config['dynamo']['table_name']
    response = client.query(
        TableName=table_name,
        KeyConditionExpression='Username = :username',
        ExpressionAttributeValues={
            ':username': {'S': username }
        }
    )
    return 0 < len(response['Items'])
