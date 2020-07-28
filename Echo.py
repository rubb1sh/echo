import imaplib
import smtplib
import re
import email
import Send
import Filter
import massage
from email.mime.text import MIMEText
from email.header import Header

server = "imap.gmail.com"
From = ''
pattern = '简历'
type = 'str'


def connect(send_mail: str, password: str):
    try:
        imapServer = imaplib.IMAP4_SSL(server)
        imapServer.login(send_mail, password)
        imapServer.select()
    except Exception:
        print("Error: can't connect server.")
        exit(1)

    return imapServer


def handle(data: list) -> (str, str):

    try:
        msg = email.message_from_string(data[0][1].decode("utf-8"))
        msgCharset = email.header.decode_header(msg.get('Subject'))[0][1]
        subject = email.header.decode_header(msg.get('Subject'))[
            0][0].decode(msgCharset)
        to_mail = msg.get('Return-Path')[1:-1]
    except Exception:
        print("Error: handle error.")
        exit(1)
    return (to_mail, subject)


def echo(send_mail: str, password: str, f: str):
    # sender's name
    From = f

    imapServer = connect(send_mail, password)

    _, items = imapServer.search(None, "Unseen")
    for item in items[0].split():
        _, data = imapServer.fetch(item, "(RFC822)")
        to_mail, subject = handle(data)
        # use re filter mail that you need to receive.
        # if Filter.Filter(subject, pattern, type):
        if Filter.minusSign(subject) or Filter.Filter(subject, pattern, type):
            print("send to:" + to_mail)
            # replyMsg = massage.Encode(From, to_mail)
            replyMsg = massage.getMsg(From, to_mail)
            Send.Send(send_mail, password, to_mail, replyMsg)
