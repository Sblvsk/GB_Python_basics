def thesaurus(*args):
    my_dict = {}
    args = [*args]
    args.sort()
    # print(args, type(args))

    for i in args:
        key, value = i[0], i
        my_dict.setdefault(key, value.split())

        if value not in my_dict[key]:
            my_dict[key].append(value)

    return print(my_dict)


# не успел дописать, пока не получается бытро найти явное решение
def thesaurus_adv(*args):
    args = [*args]
    my_dict = {}
    for i in args:
        value, key = i.split()
        key = key[0]
        my_dict.setdefault(key, i.split("  "))
        if i not in my_dict[key]:
            my_dict[key].append(i)

    # total_dict = {}
    # for key,value in my_dict.items():
    #     print(key,value)

    return print(my_dict)


thesaurus("Иван", "Мария", "Петр", "Илья", "Игорь", "Маргарита", "Андрей", "Ян")
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")