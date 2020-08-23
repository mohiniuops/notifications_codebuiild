import smtplib
from email.mime.text import MIMEText
import os
print("SMTP ACCESS Is" + os.environ['SMTP_ACCESS'])
print("SMTP PASS Is"+ os.environ['SMTP_PASS'])
html = open("template.html")
msg = MIMEText(html.read(), 'html')
text = msg.as_string()
s = smtplib.SMTP('email-smtp.us-west-2.amazonaws.com')
s.connect('email-smtp.us-west-2.amazonaws.com',587)
s.starttls()
s.login(os.environ['SMTP_ACCESS'],os.environ['SMTP_PASS'])
msg="From: mohinidevops@gmail.com \nTo: mohinidevops@gmail.com \nSubject: TestMessage \n\n Hello"
s.sendmail('mohinidevops@gmail.com','mohinidevops@gmail.com',text)




