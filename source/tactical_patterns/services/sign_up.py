"""

    >>> repository = Repository()

    >>> request = dict(email='ivanov@gmail.com', password=123)
    >>> controller = SignupController(repository)
    >>> controller.sign_up_action(request)


"""


class Repository:
    pass


class SignUpUserRequest:
    def __init__(self, email, password):
        self.email = email
        self.password = password


class SingUpService:

    def __init__(self, repository):
        self.repository = repository

    def execute(self, request: SignUpUserRequest):
        return 2


class SignupController:

    def __init__(self, repository):
        self.repository = repository

    def sign_up_action(self, request: dict):
        sign_up_service = SingUpService(self.repository)
        response = sign_up_service.execute(SignUpUserRequest(
            email=request.get('email'),
            password=request.get('password')))
