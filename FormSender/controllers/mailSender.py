import smtplib
from validate_email import validate_email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def reportMail(email, passwd, to, messageType, text):
    haveEmail = validate_email(email)
    if(not haveEmail):
        return -1
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = messageType
        msg.attach( MIMEText(text, "plain", "utf-8" ) )
        msg = msg.as_string().encode('ascii')
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(email, passwd)
        server.sendmail(email, to, msg)
        return 1
    except:
        return -2
