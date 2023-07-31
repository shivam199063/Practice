import boto3

snsAlert = boto3.client("sns")

login= int(input("if alert press :1 \n if Successfull press: 2"))

if login ==1:
    snsAlert.publish(
       Message= "Anuthorized login....",
       Subject= "Malicious Threat Actor Detected",
       TopicArn= "arn:aws:sns:ap-south-2:789757563817:Alert"
)

if login ==2:
    snsAlert.publish(
       Message= "Authorized login....",
       Subject= "User login successfully...",
       TopicArn= "arn:aws:sns:ap-south-2:789757563817:Alert"
)