cubs_list = []
for i in range(1, 1000, 2):
    cube = i ** 3
    cubs_list.append(cube)

my_list = []
sum_my_list = 0
for i in cubs_list:
    value = i
    my_sum = 0
    while value != 0:
        my_sum += value % 10
        value //= 10
    else:
        if my_sum % 7 == 0:
            my_list.append(my_sum)
            sum_my_list += i

print("Сумма чисел сумма цифр которых делится нацело на 7:", sum_my_list)

for i in range(len(cubs_list)):
    cubs_list[i] += 17

my_list = []
sum_my_list = 0
for i in cubs_list:
    value = i
    my_sum = 0
    while value != 0:
        my_sum += value % 10
        value //= 10
    else:
        if my_sum % 7 == 0:
            my_list.append(my_sum)
            sum_my_list += i
print("Сумма чисел сумма цифр которых делится нацело на 7 из обновлённого списка :", sum_my_list)
