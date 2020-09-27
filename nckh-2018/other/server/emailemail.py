import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ham import *

def sendemail(send_to_email,subject,message):

    email = docfile(4)
    passwork = docfile(5)

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, passwork)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()