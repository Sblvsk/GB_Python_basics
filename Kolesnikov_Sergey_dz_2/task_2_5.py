int_list = [57.8, 46.51, 97, 188.1, 88, 12, 1007, 1.01, 0.1, 10]
int_list.sort()

str_list = []
for i in int_list:
    str_list.append(str(i))

my_str = ""
for i in str_list:
    parts = i.split('.')
    if len(parts) == 1:
        my_str += f"{i} руб 00 коп, "
    else:
        my_str += f"{parts[0]} руб {int(parts[1]):02.0f} коп, "
my_str = my_str[:-2]
print(my_str)

new_list_rev = list(reversed(my_str.split(', ')))
print((new_list_rev[:5])[::-1])

