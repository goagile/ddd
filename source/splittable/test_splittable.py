"""

Таблица с разделителями
=======================

    >>> from splittable import SplitTable

Создание таблицы (с указанием заголовков)

    >>> headers = 'X Y Z A B'.split()
    >>> table = SplitTable(headers)

Добавление строки в таблицу

    >>> row = '@', 4, 2.1, False, 'Нет'
    >>> table.append(row)

Доступ к строке по индексу, доступ к ячейке по имени столбца

    >>> row = table[0]
    >>> row.X, row.Y, row.Z, row.A, row.B
    ('@', 4, 2.1, False, 'Нет')

Доступ к строке по индексу, доступ к ячейке по индексу столбца

    >>> row = table[0]
    >>> row[0], row[1], row[2], row[3], row[4]
    ('@', 4, 2.1, False, 'Нет')

Доступ к несуществующему атрибуту по имени столбца

    >>> row.G
    Traceback (most recent call last):
      ...
    splittable.InvalidColumnName: G

Добавление строки в таблицу

    >>> row = '&', 22, 5.03, True, 'Да'
    >>> table.append(row)

Доступ к столбцу по индексу строки

    >>> column_X = table.X
    >>> column_X[0], column_X[1]
    ('@', '&')

Доступ к несуществующей строке

    >>> column_X[10]
    Traceback (most recent call last):
      ...
    splittable.InvalidRowIndex: 10

Перебор строк и доступ к данным строки

    >>> for row in table:
    ...     row.data
    ['@', 4, 2.1, False, 'Нет']
    ['&', 22, 5.03, True, 'Да']

Перебор строк и столбцов

    >>> for row in table:
    ...     [col for col in row]
    ['@', 4, 2.1, False, 'Нет']
    ['&', 22, 5.03, True, 'Да']

"""
