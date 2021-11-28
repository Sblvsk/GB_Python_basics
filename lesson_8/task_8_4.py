from functools import wraps

def val_checker(value):
    def check(func):
        @wraps(func)
        def wrapper(args):
            if value(args):
                return print(func(args))
            else:
                raise ValueError

        return wrapper

    return check


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

a = calc_cube(5)
a = calc_cube(-5)