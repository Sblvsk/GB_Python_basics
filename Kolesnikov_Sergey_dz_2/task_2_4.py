my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in my_list:
    name = i[::-1]
    name = name[:name.index(" ")]
    name = name[::-1].capitalize()
    print(f"Привет, {name}!")
