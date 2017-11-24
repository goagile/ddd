"""

Таблица с разделителями
=======================

    >>> from splittable import SplitTable

Создание таблицы (с указанием заголовков)

    >>> headers = 'X Y Z A B'.split()
    >>> t = SplitTable(headers)
    >>> t.X

Добавление строки в таблицу

    >>> row = '@', 4, 2.1, False, 'Нет'
    >>> t.append(row)

Доступ к строке

    >>> row = t[0]
    >>> row.X, row.Y, row.Z, row.A, row.B
    ('@', 4, 2.1, False, 'Нет')

Доступ к несуществующему атрибуту

    >>> row.G
    Traceback (most recent call last):
      ...
    splittable.InvalidColumnName: G


"""
