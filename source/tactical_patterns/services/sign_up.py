"""

SingUpService
=============
Служба уровня приложения

Создаем объекты на уровне приложения

    >>> repository = Repository()
    >>> handler = SignupHandler(repository)

Эмулируем post запрос от клиента к уровню приложения

    curl post http://localhost/sign_up_action/
    >>> responce = handler.post(dict(email='ivanov@gmail.com', password=123))
    >>> isinstance(responce, dict)
    True
    >>> responce['user_id']
    11
    >>> responce['email']
    'ivanov@gmail.com'
    >>> responce['password']
    123


"""


class Repository:

    ids = iter([11, 22, 33, 44, 55])

    def user_by_email(self, email):
        pass

    def next_id(self):
        return next(self.ids)

    def add_user(self, user):
        pass


class SignUpUserRequest:
    def __init__(self, email, password):
        self.email = email
        self.password = password


class SignUpUserResponce:

    def __init__(self, user):
        self.user = user

    @property
    def user_id(self):
        return self.user.user_id

    @property
    def email(self):
        return self.user.email

    @property
    def password(self):
        return self.user.password

    def dumps(self):
        result = {
            'user_id': self.user_id,
            'email': self.email,
            'password': self.password,
        }
        return result


class UserAlreadyExistException(Exception):
    pass


class User:
    def __init__(self, user_id, email, password):
        self.user_id = user_id
        self.email = email
        self.password = password


class SingUpService:

    def __init__(self, repository):
        self.repository = repository

    def execute(self, request: SignUpUserRequest):
        user = self.repository.user_by_email(request.email)
        if user:
            raise UserAlreadyExistException

        user = User(
            self.repository.next_id(),
            request.email,
            request.password
        )

        self.repository.add_user(user)

        request = SignUpUserResponce(user)

        return request


class SignupHandler:

    def __init__(self, repository):
        self.repository = repository

    def post(self, request: dict):
        response = None

        email = request.get('email')
        password = request.get('password')

        sign_up_service = SingUpService(self.repository)

        try:
            response = sign_up_service.execute(SignUpUserRequest(email, password))
        except UserAlreadyExistException:
            print('User already exist')

        if response:
            response = response.dumps()

        return response
