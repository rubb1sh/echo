import smtplib

port = '465'
host = 'smtp.gmail.com'


# def HTMLContent() -> str:


def Send(sender: str, password: str, receiver: str, msg: str):
    try:
        smtpObj = smtplib.SMTP_SSL(host=host, port=port)
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receiver, msg.as_string())
        print("mail has been succeed to send.")
    except smtplib.SMTPException:
        print("Error: smtp can't tranlate mail")
    finally:
        smtpObj.quit()
        smtpObj.close()
