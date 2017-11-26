"""

Создания объект из словаря
==========================

Импортируем пользовательский словарь

    >>> from klass.user_dict import user_dict

Импортируем функцию создания объекта

    >>> from klass import object_from_dict

Создаем объект на основе словаря

    >>> x = object_from_dict(user_dict)

Получаем доступ к полям объекта

    >>> x.name
    'Вася'

    >>> address = x.address
    >>> address.city
    'Moscow'

    >>> for order in x.orders:
    ...     order.part, order.price
    ('Giutar', 100)

"""
