"""

    >>> user_dict = {
    ...     'name': 'Вася',
    ...     'address': {
    ...         'city': 'Moscow'
    ...     },
    ...     'заказы': [
    ...         {
    ...             'part': 'Giutar',
    ...             'price': 100
    ...         }
    ...     ]
    ... }

    >>> x = Klass.from_dict(user_dict)
    >>> x.name
    'Вася'

    >>> address = x.address
    >>> address.city
    'Moscow'

    >>> for order in x.orders:
    ...     order.part, order.price
    ('Giutar', 100)

    >>> x.build_klass_keyword()
    'class Klass:\\n'

    >>> x.build_constructor()
    '\\tdef __init__(self, address, name, orders):\\n'

    >>> z = (
    ...     '\\t\\t'
    ...     'self.address = address'
    ...     '\\n\\t\\t'
    ...     'self.name = name'
    ...     '\\n\\t\\t'
    ...     'self.orders = orders'
    ...     '\\n'
    ... )
    >>> z == x.build_fields()
    True

    >>> x.save('x.py')

"""


class Klass:

    blank = '\n'
    tab = '    '

    @classmethod
    def from_dict(cls, user_dict):
        result = Klass()
        for key, value in user_dict.items():
            field = value
            if isinstance(value, dict):
                field = cls.from_dict(value)
            elif isinstance(value, list):
                field = [cls.from_dict(f) for f in value]
            setattr(result, key, field)
        return result

    def save(self, filename):
        rows = [
            self.build_klass_keyword(),
            self.build_constructor(),
            self.build_fields()
        ]
        with open(filename, 'w') as f:
            f.writelines(rows)

    def build_klass_keyword(self):
        klass_keyword_template = 'class Klass:{blank}'
        result = klass_keyword_template.format(blank=self.blank)
        return result

    def build_constructor(self):
        constructor_template = '{tabs}def __init__(self, {args}):{blank}'
        result = constructor_template.format(
            tabs=self.tab,
            args=self.__get_args_names(),
            blank=self.blank)
        return result

    def __get_args_names(self):
        return ', '.join(sorted(self.__dict__.keys()))

    def build_fields(self):
        result = [self.__build_field(name) for name in sorted(self.__dict__.keys())]
        return ''.join(result)

    def __build_field(self, name):
        field_template = '{tabs}self.{name} = {value}{blank}'
        result = field_template.format(
            tabs=self.tab + self.tab,
            name=name,
            value=name,
            blank=self.blank
        )
        return result
