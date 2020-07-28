import re

# filter strategy RE

# 使用- -分隔


def minusSign(s: str) -> bool:
    ss = s.split("-")
    if len(ss) == 3:
        return True
    return False


def Filter(s: str, sub: str, type: str) -> bool:
    if type.lower() == 're':
        return re_filter(s, sub)
    elif type.lower() == 'str':
        return str_filter(s, sub)


def re_filter(s: str, pattern: str) -> bool:
    if re.match(pattern, s):
        return True
    return False


def str_filter(s: str, sub: str) -> bool:
    if sub in s:
        return True
    return False
