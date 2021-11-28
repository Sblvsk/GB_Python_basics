
def type_logger(func):
    def wrapper(*args):
        result = str(*args)
        print(f'{func.__name__}({result}: <{type(func(*args))}>)')
        return result

    return wrapper

@type_logger
def calc_cube(x):
    return x ** 3

a = calc_cube(5)
