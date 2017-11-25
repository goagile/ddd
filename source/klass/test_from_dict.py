"""

    >>> user_dict = {
    ...     'name': 'Вася',
    ...     'address': {
    ...         'city': 'Moscow',
    ...         'country': {
    ...             'caption': 'Russia'
    ...         }
    ...     },
    ...     'orders': [
    ...         {
    ...             'part': 'Giutar',
    ...             'price': 100
    ...         }
    ...     ]
    ... }

    >>> x = object_from_dict(user_dict)
    >>> x.name
    'Вася'

    >>> address = x.address
    >>> address.city
    'Moscow'

    >>> for order in x.orders:
    ...     order.part, order.price
    ('Giutar', 100)

Строим описание класса

    >>> builder = KlassBuilder()
    >>> builder.build_klass_keyword(x)
    'class Klass:\\n'

    >>> builder.build_constructor(x)
    '    def __init__(self, address, name, orders):\\n'

    >>> builder.build_fields(x)
    '        self.address = address\\n        self.name = name\\n        self.orders = orders\\n'

    >>> builder.save(x, 'x.py')

"""


class Klass:
    pass


def object_from_dict(user_dict):
    result = Klass()
    for key, value in user_dict.items():
        field = value
        if isinstance(value, dict):
            field = object_from_dict(value)
        elif isinstance(value, list):
            field = [object_from_dict(f) for f in value]
        setattr(result, key, field)
    return result


class KlassBuilder:

    blank = '\n'
    tab = '    '
    klass_keyword_template = 'class Klass:{blank}'
    constructor_template = '{tabs}def __init__(self, {args}):{blank}'
    field_template = '{tabs}self.{name} = {value}{blank}'

    def build(self, obj):
        result = [
            self.blank,
            self.blank,
            self.build_klass_keyword(obj),
            self.build_constructor(obj),
            self.build_fields(obj)
        ]
        return result

    def build_klass_keyword(self, obj):
        result = self.klass_keyword_template.format(blank=self.blank)
        return result

    def build_constructor(self, obj):
        result = self.constructor_template.format(
            tabs=self.tab,
            args=self.__get_args_names(obj),
            blank=self.blank)
        return result

    def __get_args_names(self, obj):
        return ', '.join(sorted(obj.__dict__.keys()))

    def extend_from_fields(self, obj, rows):
        for field in obj.__dict__.values():
            if isinstance(field, Klass):
                rows.extend(self.build(field))
                self.extend_from_fields(field, rows)
            elif isinstance(field, list):
                for f in field:
                    self.extend_from_fields(f, rows)

    def build_fields(self, obj):
        result = [self.__build_field(name) for name in sorted(obj.__dict__.keys())]
        return ''.join(result)

    def __build_field(self, name):
        result = self.field_template.format(
            tabs=self.tab + self.tab,
            name=name,
            value=name,
            blank=self.blank
        )
        return result

    def save(self, obj, filename):
        rows = self.build(obj)
        self.extend_from_fields(obj, rows)
        with open(filename, 'w') as f:
            f.writelines(rows)
