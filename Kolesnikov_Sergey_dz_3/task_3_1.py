
def num_translate(value):
    value = value.lower() if value.islower() else value.capitalize()
    values = {
        "zero": "ноль",
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять"
    }
    if value.islower():
        return print(values.get(value))
    else:
        return print(values.get(value.lower()).capitalize())

num_translate("One")
num_translate("eight")
num_translate("Ten")
