import argparse
import re


mail_re = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'


def paramDecode():
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', type=str, required=True,
                        help='your@email.com')
    parser.add_argument('--password', type=str,
                        required=True, help='email password')
    # parser.add_argument('--server', type=str, required=True,
    #                    help='email server(if @163.com, it will be imap.163.com')
    parser.add_argument('--From', type=str,
                        required=True, help='your name')
    # Print usage
    args = parser.parse_args()

    if not re.match(mail_re, args.email):
        raise Exception
    return args
