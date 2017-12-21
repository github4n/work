import re


m = re.search('^The', 'The end.')
if m is not None:
    print(m.group())