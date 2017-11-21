"""

    >>> pid = '2911045806'
    >>> p = Person(pid, 'Петров-Водкин', 'Иван')

"""


class Person:

    def __init__(self, person_id, last_name, first_name):
        self.person_id = person_id
        self.last_name = last_name
        self.first_name = first_name
