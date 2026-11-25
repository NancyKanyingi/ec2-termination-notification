import json
import boto3
import os

def lambda_handler(event, context):
    sns_client = boto3.client('sns')
    sns_topic_arn = os.getenv('SNS_TOPIC_ARN')
    
    # Extract EC2 details from the event
    detail = event.get('detail', {})
    instance_id = detail.get('instance-id', 'N/A')
    state = detail.get('state', 'N/A')

    # Build message content
    message = f"EC2 Instance Terminated\n\nInstance ID: {instance_id}\nState: {state}"
    subject = "EC2 Instance Termination Alert"

    # Publish to SNS topic
    response = sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=message,
        Subject=subject
    )
    
    print("Notification sent:", response)
    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent successfully!')
    }