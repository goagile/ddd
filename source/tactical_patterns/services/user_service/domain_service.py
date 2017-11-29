"""

User
====
Служба предметной области

имеются объекты предметной области

    >>> class User:
    ...     def sign_up(self, username, password):
    ...         pass

    >>> class Cart:
    ...     def create_order(self):
    ...         pass

Объект User не должен иметь обязанности по входу в систему
Выделим для этого отдельную службу

    >>> class SignUp:
    ...     def execute(self, username, password):
    ...         self.username = username
    ...         self.password = password

    >>> s = SignUp()
    >>> s.execute('петрович', 123)

Служба, которая создает заказ на основании корзины

    >>> class Cart:
    ...     def __init__(self):
    ...         pass

    >>> class CreateOrderFromCart:
    ...     def execute(self, cart):
    ...         pass

    >>> c = CreateOrderFromCart()
    >>> cart = Cart()
    >>> c.execute(cart)

"""
