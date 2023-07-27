import smtplib,getpass

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("2002636.cse.cec@cgc.edu.in", getpass.getpass("Enter your Email Password: "))

subject="Hello Message"
# message to be sent
message = f"SUBJECT: {subject} \n\nMy name is Shivam Saini"

# sending the mail
s.sendmail("2002636.cse.cec@cgc.edu.in", "shivam199063@gmail.com", message)

# terminating the session
s.quit()
