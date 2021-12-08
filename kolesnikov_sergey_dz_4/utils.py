from requests import get, utils

def currency_rates(currency):
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    key_list = content.split('<CharCode>')
    key_list = key_list[1:]
    values = {}
    for i in key_list:
        str_in_float = ".".join((i[i.index("/Value")-8:i.index("</Value")]).split(","))
        values.setdefault(i[:3], float(str_in_float))

    return print(values.get(currency))

if __name__ == "__main__":
    import sys
    currency_rates(sys.argv[1])