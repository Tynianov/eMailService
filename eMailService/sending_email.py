import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(send_to_email,message):
    email = 'send.sweet.words@gmail.com'
    password = 'Sasha123Bob'

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = 'Aanonymous letter from someone who loves you <3 <3 <3'

    msg.attach(MIMEText(message))

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email,send_to_email,text)
    server.quit()