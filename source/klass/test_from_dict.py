

def from_dict(user_dict):
    class Klass(object):
        pass
    for key, value in user_dict.items():
        field = value
        if isinstance(value, dict):
            field = from_dict(value)
        elif isinstance(value, list):
            field = [from_dict(f) for f in value]
        setattr(Klass, key, field)
    return Klass


if __name__ == '__main__':
    user_dict = {
        'name': 'Вася',
        'address': {
            'city': 'Moscow'
        },
        'orders': [
            {
                'part': 'Giutar',
                'price': 100
            }
        ]
    }
    x = from_dict(user_dict)
    print(x)
    print(x.name)
    print(x.address)
    print(x.address.city)
    print(x.orders)
    print(x.orders[0])
    print(x.orders[0].part)
    print(x.orders[0].price)
