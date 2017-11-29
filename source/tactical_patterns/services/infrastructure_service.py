"""

Интерфейс публикуется на уровне предметной области
А реализуется на уровне инфраструктуры

    >>> user_repository = UserRepository()
    >>> service = DefaultHashingSignUp(user_repository)
    >>> user = service.execute('daniel', 123)
    Traceback (most recent call last):
      ...
    ValueError: The user daniel does not exist


    >>> user_repository.add_user('daniel', 123)
    >>> user = service.execute('daniel', 123)
    >>> user
    User(username=daniel, password=123)

"""


import abc


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


class SignUp(abc.ABC):
    def execute(self, username: str, password: str):
        pass


class BadCredentialsException(Exception):
    pass


class DefaultHashingSignUp(SignUp):
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, username: str, password: str):
        if not self.user_repository.has_user(username):
            raise ValueError('The user {} does not exist'.format(username))
        user = self.user_repository.by_user_name(username)
        if not self.is_password_valid_for_user(user, password):
            raise BadCredentialsException('{}; {}'.format(username, password))
        return user

    @classmethod
    def is_password_valid_for_user(cls, user, password):
        return password_verify(password, hash(user))


def password_verify(password, user_hash):
    return True
