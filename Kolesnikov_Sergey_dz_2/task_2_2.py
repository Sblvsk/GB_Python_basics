my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_str = ''

for i in my_list:
    if i.isdigit():
        new_str += f'"{int(i):02.0f}" '
    elif i[1:].isdigit():
        new_str += f'"{i[:1]}{int(i):02.0f}" '
    else:
        new_str += f'{i} '
print(new_str)