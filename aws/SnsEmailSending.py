import boto3

# Initialize the SNS client
snsObject = boto3.client("sns")
    
    
snsObject.publish(
        Message="Hello my name is Shivam Saini",
        Subject="Introduction of Employee",
        TopicArn="arn:aws:sns:ap-south-2:789757563817:Alert"
    )
