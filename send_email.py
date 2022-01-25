#Libraries
import smtplib
import ssl 
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

subject = "Email from Kaszuby"
body = "This is a test email from Kaszuby!"
sender_email = "workharder1000000@gmail.com"
receiver_email = "workharder1000000@gmail.com"
password = input("enter a password: ")                 

#building the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body) 

context = ssl.create_default_context() #we need a secure connection while connecting to Gmail

print("Sending Email!")

#port 465 - secure e-mail sending with SSL - this port is no longer used
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
  server.login(sender_email, password) #logging to server
  server.sendemail(sender_email, receiver_email, message.as string)
  
print("Success")
  
#possible improvements - sending files, sending to multiple people
