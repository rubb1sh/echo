from email.mime.text import MIMEText
from email.header import Header

# content = '已收到您的简历'
subject = '扫描邮件中的二维码，对您的简历进行内推.'
charset = 'utf-8'


def getContent() -> str:
    file = open('content.html')
    content = file.read()
    return content


def Encode(From: str, To: str, content: str) -> str:
    message = MIMEText(content, 'plain', charset)
    message['From'] = Header(From, charset)
    message['To'] = Header(To, charset)
    message['Subject'] = Header(subject, charset)
    return message


def getMsg(From: str, To: str) -> str:
    content = getContent()
    message = MIMEText(content, 'html', charset)
    message['From'] = Header(From, charset)
    message['To'] = Header(To, charset)
    message['Subject'] = Header(subject, charset)
    return message
