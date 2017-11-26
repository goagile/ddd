import re


INVALID_ISO_CODE = 'Invalid Iso code'


class CurrencyModel:

    iso_code_pattern = re.compile('^[A-Z]{3}$')

    def __init__(self, iso_code, sign):
        self.__iso_code = self.__set_iso_code(iso_code)
        self.__sign = sign

    def __repr__(self):
        return self.iso_code

    @property
    def sign(self):
        return self.__sign

    @property
    def iso_code(self):
        return self.__iso_code

    def __set_iso_code(self, value):
        self.__validate_iso_code(value)
        return value

    def __validate_iso_code(self, value):
        if not self.iso_code_pattern.match(value):
            raise ValueError(INVALID_ISO_CODE)
