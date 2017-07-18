import codecs

if __name__ == '__main__':
    path = 'test.po'
    with open(path, "r") as file:
        lines = file.readlines()
    print(lines)
