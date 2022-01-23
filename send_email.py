#Libraries
import smtplib
import ssl 
from email.message import EmailMessage

subject = "Email from Kaszuby"
body = "This is a test email from Kaszuby!"
sender_email = "workharder1000000@gmail.com"
receiver_email = "workharder1000000@gmail.com"
password = input("enter a password: ")

#building the email
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body) 

context = ssl.create_default_context() #we need a secure connection while connecting to Gmail







#possible improvements - sending files, sending to multiple people
