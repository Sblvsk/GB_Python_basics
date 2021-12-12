

def generator_odd_numbs(number):
    for num in range(1,number + 1, 2):
        yield num


odd_to_15 = generator_odd_numbs(15)
print(next(odd_to_15))
print(odd_to_15.__next__())
