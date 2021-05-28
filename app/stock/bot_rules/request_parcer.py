import re

def stock_parser(text):
    result = re.search('(:\d{2}),(.*)\\r', text)
    resulted_string = result.group(2)
    if not resulted_string:
        return ""
    return resulted_string