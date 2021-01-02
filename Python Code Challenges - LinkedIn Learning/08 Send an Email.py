# Challenge: Write a Python function to send a basic email notification.
# Input: receiver email address, subject line, message body


# IMPORTANT: Set sender email information prior to running file (for easier use)
# For the function to work successfully, access for less secure apps must be turned on for the sender email

import smtplib, ssl

SENDER_EMAIL = ""
SENDER_PASSWORD = ""

def sendEmail(receiver, subject, body):
    newContext = ssl.create_default_context()

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=newContext)        # Set up secure connection

    try:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver, "Subject: {}\n\n{}".format(subject, body))
    except:
        print("Login failed")

    server.quit()

receiverEmail = input()
emailSubject = input()
emailBody = input()
# receiverEmail = "joshuajohnson0311@mail.com"
# emailSubject = "Testing my Python Function"
# emailBody = "This is awesome!"

sendEmail(receiverEmail, emailSubject, emailBody)
