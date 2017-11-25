"""

Таблица с разделителями
=======================

Подключаем таблицу

    >>> from tablo.split_tablo import SplitTablo

    >>> t = SplitTablo(' X  Y  Z  A  B '.split())
    >>> t.append('  @  4   2.1   False  Нет   '.split())
    >>> t.append('  $  5.2   8   True    Да   '.split())

Авто-выравнивание ширины колонок

    >>> t = SplitTablo(' X  Y  Z  A  B '.split())
    >>> t.append('  @  4   2.1   False  Нет   '.split())
    >>> t.append('  $  5.2   8   True    Да   '.split())

    >>> for x in t.print():
    ...     x
    '|@|4  |2.1|False|Нет|'
    '|$|5.2|8  |True |Да |'

Ручное выравнивание + автовыравнивание колонки

    >>> t.X.margin = 10
    >>> t.B.margin = 15

    >>> [name for name in t.columns]
    ['X', 'Y', 'Z', 'A', 'B']

    >>> for name, column in t.columns.items():
    ...     column.margin
    10
    3
    3
    5
    15

    >>> for x in t.print():
    ...     x
    '|@         |4  |2.1|False|Нет            |'
    '|$         |5.2|8  |True |Да             |'

# Строковое представление строки
#
#     >>> for row in t:
#     ...     str(row)
#     '|@|4|2.1|False|Нет|'
#     '|@|56|3.02|True|Брахмапутра|'

# Печать всех строк
#
#     >>> t.print()
#     '|@|4 |2.1 |False|Нет        |'
#     '|@|56|3.02|True |Брахмапутра|'

"""
