"""

Интерфейс публикуется на уровне предметной области
А реализуется на уровне инфраструктуры

    >>> import abc

    >>> class SignUp(abc.ABC):
    ...     def execute(self, username: str, password: str):
    ...         pass

"""
