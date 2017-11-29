"""

Интерфейс публикуется на уровне предметной области
А реализуется на уровне инфраструктуры

    >>> user_repository = UserRepository()
    >>> service = DefaultHashingSignUp(user_repository)
    >>> user = service.execute('daniel', 123)


"""


import abc


class UserRepository:

    def by_user_name(self, username):
        pass

    def has_user(self, username):
        pass


class SignUp(abc.ABC):
    def execute(self, username: str, password: str):
        pass


class BadCredentialsException(Exception):
    pass


class DefaultHashingSignUp(SignUp):
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, username: str, password: str):
        if self.user_repository.has_user(username):
            raise ValueError('The user {} does not exist'.format(username))
        user = self.user_repository.by_user_name(username)
        if not self.is_password_valid_for_user(user, password):
            raise BadCredentialsException('{}; {}'.format(username, password))
        return user

    @classmethod
    def is_password_valid_for_user(cls, user, password):
        return password_verify(password, hash(user))


def password_verify(password, user_hash):
    pass
