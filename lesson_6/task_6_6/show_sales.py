def show(argv):
    with open('bakery.csv', encoding='utf-8') as f:
        if len(argv) == 1:
            show_file = f.read()
            print(show_file)
        elif len(argv) == 2:
            start = int(argv[1])
            file_to_str = f.read()
            paragraphs = file_to_str.splitlines()
            conclusion = [print(z) for i, z in enumerate(paragraphs, 1) if i >= start]
        else:
            start = int(argv[1])
            stop = int(argv[2])
            file_to_str = f.read()
            paragraphs = file_to_str.splitlines()
            conclusion = [print(z) for i, z in enumerate(paragraphs, 1) if i >= start and i<= stop]
    return 0

if __name__ == "__main__":
    import sys
    exit(show(sys.argv))
