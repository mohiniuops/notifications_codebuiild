import smtplib
from email.mime.text import MIMEText
import boto3
import os
print("SMTP ACCESS Is" + os.environ['SMTP_ACCESS'])
print("SMTP PASS Is"+ os.environ['SMTP_PASS'])


