"""

    >>> repository = OrderRepository(create_fake_id)
    >>> nid = repository.next_identity()
    >>> str(nid)
    '1'

    >>> repository.generate_id = create_uid
    >>> uid = repository.next_identity()


"""

import uuid


ids = iter([1, 2, 3, 4])


def create_fake_id():
    id_ = next(ids)
    return OrderId(id_)


def create_uid():
    uid = uuid.uuid4()
    return OrderId(uid)


class OrderId:

    def __init__(self, id_):
        self.id_ = id_

    def __str__(self):
        return '{}'.format(self.id_)


class OrderRepository():

    def __init__(self, generate_id):
        self.generate_id = generate_id

    def next_identity(self):
        return self.generate_id()
