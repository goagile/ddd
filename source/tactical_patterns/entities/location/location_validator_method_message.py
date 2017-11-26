"""

Проверяем как обработчик ошибок печатает сообщения

    >>> handler = LocationValidationHandler()
    >>> handler.handle_city_not_found_country()
    City not found
    >>> handler.handle_invalid_post_code_for_city()
    Postcode is invalid

Создаем валидный адрес

    >>> postcode = '123-456'
    >>> moscow = City('Moscow')
    >>> moscow.add_postcode(postcode)
    >>> ru = Country('Russia')
    >>> ru.add_city(moscow)
    >>> location = Location(ru, moscow, postcode)
    >>> location.validate(handler)

Создаем адрес с невалидным Городом

    >>> postcode = '123-456'
    >>> moscow = City('Moscow')
    >>> moscow.add_postcode(postcode)
    >>> ru = Country('Russia')
    >>> ru.add_city(moscow)
    >>> newyork = City('New-Yourk')
    >>> location = Location(ru, newyork, postcode)
    >>> location.validate(handler)
    City not found

Создаем адрес с невалидным Индексом

    >>> postcode = '123----456'
    >>> moscow = City('Moscow')
    >>> moscow.add_postcode(postcode)
    >>> ru = Country('Russia')
    >>> ru.add_city(moscow)
    >>> location = Location(ru, moscow, postcode)
    >>> location.validate(handler)
    Postcode is invalid

"""

import re


class ValidationHandler:

    def __init__(self):
        pass

    def handle_error(self, message):
        print(message)


class LocationValidationHandler(ValidationHandler):

    def handle_city_not_found_country(self):
        self.handle_error('City not found')

    def handle_invalid_post_code_for_city(self):
        self.handle_error('Postcode is invalid')


class AbstractValidator:

    def __init__(self, validation_handler):
        self.validation_handler = validation_handler

    def handle_error(self, message):
        self.validation_handler.handle_error(message)

    def valildate(self):
        pass


class LocationValidator(AbstractValidator):

    def __init__(self, location, validation_handler):
        super().__init__(validation_handler)
        self.location = location

    def valildate(self):
        city = self.location.city
        if not self.location.country.has_city(city.name):
            self.validation_handler.handle_city_not_found_country()

        postcode = self.location.postcode
        if not self.location.city.is_postcode_valid(postcode):
            self.validation_handler.handle_invalid_post_code_for_city()


class City:

    def __init__(self, name):
        self.name = name
        self.postcodes = []
        self.format = re.compile('^(\d){3}-(\d){3}$')

    def add_postcode(self, postcode):
        self.postcodes.append(postcode)

    def is_postcode_valid(self, postcode):
        return bool(self.format.match(postcode))


class Country:

    def __init__(self, name):
        self.name = name
        self.cities = {}

    def add_city(self, city: City):
        name = city.name
        self.cities[name] = city

    def has_city(self, name):
        return bool(self.cities.get(name, False))


class Location:

    def __init__(self, country, city, postcode):
        self.country = country
        self.city = city
        self.postcode = postcode

    def validate(self, validation_handler):
        validator = LocationValidator(location=self, validation_handler=validation_handler)
        validator.valildate()
