from email import message
#import imp
from multiprocessing import context
import smtplib
import ssl
from email.message import EmailMessage

subject = "MY PYTHON EMAIL"
body = "This is my python email"
sender_email = "kliqsuperuser001@gmail.com"
reciever_email = "kliqsuperuser001@gmail.com"
password = input("Input your password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = reciever_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending...")

with smtplib.SMTP_SSL("smtp.gmail.com", 456, context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email, reciever_email, message.as_string)

print("Success")