import re

INVALID_ISO_CODE = 'Invalid Iso code'


class Currency:

    iso_code_pattern = re.compile('^[A-Z]{3}$')

    def __init__(self, iso_code):
        self.__iso_code = None
        self.iso_code = iso_code

    def __repr__(self):
        return self.iso_code

    @property
    def iso_code(self):
        return self.__iso_code

    @iso_code.setter
    def iso_code(self, value):
        self.validate_iso_code(value)
        self.__iso_code = value

    def validate_iso_code(self, value):
        if not self.iso_code_pattern.match(value):
            raise ValueError(INVALID_ISO_CODE)
