"""

Таблица с разделителями
=======================

Подключаем таблицу

    >>> from tablo.split_tablo import SplitTablo

Авто-выравнивание ширины колонок

    >>> t = SplitTablo('X  Y  Z  A  B'.split())
    >>> t.append('@ 4   2.1 False Нет'.split())
    >>> t.append('$ 5.2 8   True  Да '.split())

    >>> t.print()
    |@|4  |2.1|False|Нет|
    |$|5.2|8  |True |Да |

Ручное выравнивание + автовыравнивание колонки

    >>> t.X.margin = 10
    >>> t.X.centred()
    >>> t.B.margin = 15
    >>> t.B.centred()

    >>> [name for name in t.columns]
    ['X', 'Y', 'Z', 'A', 'B']

    >>> for name, column in t.columns.items():
    ...     column.margin
    10
    3
    3
    5
    15

    >>> t.print()
    |    @     |4  |2.1|False|      Нет      |
    |    $     |5.2|8  |True |      Да       |


"""
