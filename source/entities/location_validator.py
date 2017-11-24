"""

Создаем валидный адрес

    >>> moscow = Location(country='Russia', city='Moscow', postcode='12345')

Абстрактный Валидотор не разрешается создавать

    >>> av = AbstractValidator()
    Traceback (most recent call last):
      ...
    TypeError: Can't instantiate abstract class AbstractValidator with abstract methods handle_error, valildate

    >>> vh = ValidationHandler()
    >>> vh.handle_error('XXX')
    XXX


"""

import abc


class ValidationHandler:

    def handle_error(self, message):
        print(message)


class AbstractValidator(abc.ABC):

    def __init__(self, validation_handler):
        self.validation_handler = validation_handler

    @abc.abstractmethod
    def handle_error(self, message):
        self.validation_handler.handle_error(message)

    @abc.abstractmethod
    def valildate(self):
        pass


class LocationValidator(AbstractValidator):

    def __init__(self, location, validation_handler):
        super().__init__(validation_handler)
        self.location = location

    def valildate(self):
        city = self.location.city
        if not self.location.country.has_city(city):
            self.handle_error('City not found')


class Location:

    def __init__(self, country, city, postcode):
        self.country = country
        self.city = city
        self.postcode = postcode

    def validate(self, validation_handler):
        validator = LocationValidator(location=self, validation_handler=validation_handler)
        validator.valildate()
