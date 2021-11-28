with open('log.txt', encoding='utf-8') as f:
    line = f.readline()

    pars = []
    while line:
        x = [x for x in line.split()]
        my_tuple = (x[0], x[5], x[6])
        pars.append(my_tuple)
        line = f.readline()

print(pars)