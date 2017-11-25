"""

Создание класса из словаря
==========================

Импортируем пользовательский словарь
    >>> from klass.user_dict import user_dict

Подключаем построитель класса

    >>> from klass import object_from_dict, KlassBuilder

Создаем объект на основе словаря

    >>> x = object_from_dict(user_dict)

Строим описание класса

    >>> builder = KlassBuilder()
    >>> builder.build_klass_keyword(x)
    'class Klass:\\n'

    >>> builder.build_constructor(x)
    '    def __init__(self, address, name, orders):\\n'

    >>> builder.build_fields(x)
    '        self.address = address\\n        self.name = name\\n        self.orders = orders\\n'

    >>> builder.save(x, 'gen.py')

"""
