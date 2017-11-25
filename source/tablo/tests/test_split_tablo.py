"""

Таблица с разделителями
=======================

Подключаем таблицу

    >>> from tablo.split_tablo import SplitTablo

    >>> t = SplitTablo('X  Y  Z  A  B'.split())
    >>> t.append_row('@ 4   2.1 False Нет'.split())
    >>> t.append_row('$ 5.2 8   True  Да '.split())

Печать таблицы (Авто-выравнивание ширины колонок)

    # >>> [x for x in dir(t[0]) if not x.startswith('_')]

    >>> t.print()
    | X | Y   | Z   | A     | B   |
    | @ | 4   | 2.1 | False | Нет |
    | $ | 5.2 | 8   | True  | Да  |

Ручное выравнивание + автовыравнивание колонки

    >>> t.X.margin = 10
    >>> t.X.centred()
    >>> t.B.margin = 15
    >>> t.B.centred()

    >>> t.A.not_spaced()

    >>> t.print()
    |     X      | Y   | Z   |A    |        B        |
    |     @      | 4   | 2.1 |False|       Нет       |
    |     $      | 5.2 | 8   |True |       Да        |

"""
