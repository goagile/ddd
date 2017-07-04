import os

import re

RU_CONSTANT_TEXT_PATTERN = r'(?:\'|\")([-А-Яа-я \d.:?!\\|/]*)(?:\'|\")'


def collect_constants(path):
    lines = get_lines(path)
    constants = get_constants(lines)

    for constant in constants:
        print(transliterate(constant))


def transliterate(text):
    match = []
    ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧЪЫЬЭЮЯ'
    en = 'ABVGDEEJZIIKLMNOPRSTUFHCC_Y_EUY'
    for symbol in text.strip():
        case = symbol.upper()
        if case in ru:
            i = ru.index(case)
            match.append(en[i])
        elif case in ' -.:?!\\|/':
            match.append('_')
        else:
            match.append(symbol)
    result = ''.join(match).strip('_')
    return result


def get_lines(path):
    with open(path, 'r') as file:
        result = file.readlines()
    return result


def get_constants(lines):
    result = []
    for line in lines:
        result.extend(match_constant(line))
    return result


def match_constant(line):
    match = re.findall(RU_CONSTANT_TEXT_PATTERN, line)
    if match:
        return (m for m in match if m)
    return []


if __name__ == '__main__':
    js_file_name = 'file_to_translate.js'
    path = os.path.join(os.path.split(__file__)[0], js_file_name)
    collect_constants(path)
