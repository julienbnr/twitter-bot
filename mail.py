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
