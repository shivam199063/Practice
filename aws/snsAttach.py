# import boto3

# snsAlert = boto3.client("sns")

# login= int(input("if alert press :1 \n if Successfull press: 2"))

# if login ==1:
#     snsAlert.publish(
#        Message= "Anuthorized login....",
#        Subject= "Malicious Threat Actor Detected",
#        TopicArn= "arn:aws:sns:ap-south-2:789757563817:Alert"
# )

# if login ==2:
#     snsAlert.publish(
#        Message= "Authorized login....",
#        Subject= "User login successfully...",
#        TopicArn= "arn:aws:sns:ap-south-2:789757563817:Alert"
# )




import boto3

# Initialize the SNS client
snsAlert = boto3.client("sns")

def check_credentials(user_id, password):
    # Dictionary containing user ID-password pairs (Replace with your own data)
    credentials = {
        'user1': 'password1',
        'user2': 'password2',
        'user3': 'password3'
    }

    # Check if the user ID exists in the credentials dictionary
    if user_id in credentials:
        # If the provided password matches the password associated with the user ID
        if password == credentials[user_id]:
            return True
    return False

def send_alert(message, subject):
    # Replace the TopicArn with your own SNS topic ARN
    snsAlert.publish(
        Message=message,
        Subject=subject,
        TopicArn="arn:aws:sns:ap-south-2:789757563817:Alert"
    )
def main():
    user_id = input("Enter your user ID: ")
    password = input("Enter your password: ")

    if check_credentials(user_id, password):
        print("Access granted!")
    else:
        print("Access denied!")
        # Send an alert to the admin
        send_alert("Unauthorized login attempt", "Malicious Threat Actor Detected")

if __name__ == "__main__":
    main()