def add(argv):
    program, arg = argv
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{arg}\n')
    return 0

if __name__ == "__main__":
    import sys
    exit(add(sys.argv))