import boto3

from datetime import datetime
from util import str_list_to_join_string

# add an item in the table
def add_item(config, user_tweet):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(config['dynamo']['table_name'])
    table.put_item(
        Item = {
            'Username' : user_tweet.user_name,
            'LastTweet' : user_tweet.last_tweet,
            'Keywords' : str_list_to_join_string(user_tweet.keywords),
            'Date' : str(datetime.now()),
            'WebsiteUrl' : user_tweet.url
        }
    )

# check if db contains item
def has_item(config, username):
    client = boto3.client('dynamodb')
    response = client.query(
        TableName=config['dynamo']['table_name'],
        KeyConditionExpression='Username = :username',
        ExpressionAttributeValues={
            ':username': {'S': username }
        }
    )
    return 0 < len(response['Items'])
