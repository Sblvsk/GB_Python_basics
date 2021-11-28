import re

regex = re.compile(r"(?P<username>[a-zA-Z0-9]+)@(?P<domain>[a-zA-Z0-9]+\.\w+)")

def email_parse(email_adress):
    print(*map(lambda x: x.groupdict(), regex.finditer(email_adress)))

email_parse('someone@geekbrains.ru')