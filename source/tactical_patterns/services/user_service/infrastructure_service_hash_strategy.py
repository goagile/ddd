"""

Интерфейс публикуется на уровне предметной области
А реализуется на уровне инфраструктуры

    >>> user_repository = UserRepository()
    >>> service = SignUp(user_repository, DefaultHashingVerifyingStrategy())
    >>> user = service.execute('daniel', 123)
    Traceback (most recent call last):
      ...
    ValueError: The user daniel does not exist


    >>> user_repository.add_user('daniel', 123)
    >>> user = service.execute('daniel', 123)
    >>> user
    User(username=daniel, password=123)

    >>> service = SignUp(user_repository, Md5HashingVerifyingStrategy())
    >>> user = service.execute('daniel', 123)
    User(username=daniel, password=123)

"""


import abc
import hashlib


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __hash__(self):
        return hash('{}{}'.format(self.username, self.password))

    def __repr__(self):
        return 'User(username={}, password={})'.format(self.username, self.password)


class UserRepository:

    users = {}

    def add_user(self, username, password):
        self.users[username] = User(
            username=username,
            password=password)

    def by_user_name(self, username):
        return self.users.get(username)

    def has_user(self, username):
        return username in self.users


class BadCredentialsException(Exception):
    pass


class SignUp:

    def __init__(self, user_repository, verifying_strategy):
        self.user_repository = user_repository
        self.verifying_strategy = verifying_strategy

    def execute(self, username: str, password: str):
        if not self.user_repository.has_user(username):
            raise ValueError('The user {} does not exist'.format(username))

        user = self.user_repository.by_user_name(username)
        if not self.verifying_strategy.is_password_valid_for_user(user, password):
            raise BadCredentialsException('{}; {}'.format(username, password))

        return user


class DefaultHashingVerifyingStrategy:

    @classmethod
    def is_password_valid_for_user(cls, user, password):
        return True


class Md5HashingVerifyingStrategy:

    SALT = 'S0m3S41T'

    def is_password_valid_for_user(self, user, password):
        encrypted_password = hashlib.md5('{}_{}'.format(password, self.salt()).encode())
        return hash(user) == encrypted_password

    def salt(self):
        return hashlib.md5(self.SALT.encode())
