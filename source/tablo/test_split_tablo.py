"""

Таблица с разделителями
=======================

Подключаем таблицу

    >>> from tablo import SplitTablo

    >>> t = SplitTablo(' X  Y  Z  A  B '.split())
    >>> rows = (
    ...    '  @  4   2.1   False  Нет   '.split(),
    ...    '  @  56  3.02  True   Брахмапутра    '.split(),
    ... )
    >>> for r in rows:
    ...     t.append(r)

Строковое представление строки

    >>> for row in t:
    ...     str(row)
    '|@|4|2.1|False|Нет|'
    '|@|56|3.02|True|Брахмапутра|'

Печать всех строк

    >>> t.print()
    '|@|4 |2.1 |False|Нет        |'
    '|@|56|3.02|True |Брахмапутра|'

"""
