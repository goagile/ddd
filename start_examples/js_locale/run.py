import os


def collect_constants(path):
    lines = get_lines(path)

    print(''.join(lines))


def get_lines(path):
    lines = []
    with open(path, 'r') as file:
        lines = file.readlines()
    return lines


if __name__ == '__main__':
    js_file_name = 'file_to_translate.js'
    path = os.path.join(os.path.split(__file__)[0], js_file_name)
    collect_constants(path)
