import boto3

# Initialize the SNS client
snsObject = boto3.client("sns")
    
    
snsObject.publish(
        Subject="Introduction of Employee",
        Message="Hello my name is Shivam Saini",
        TopicArn="arn:aws:sns:ap-south-2:789757563817:AlertTopic"
    )
