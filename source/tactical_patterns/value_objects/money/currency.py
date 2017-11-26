from tactical_patterns.value_objects.money.currency_model import CurrencyModel


ISO_CODE_NOT_FOUND = 'Iso code not found'


class Currency:
    USD = CurrencyModel('USD', sign='$')
    RUR = CurrencyModel('RUR', sign='₽')

    @classmethod
    def from_iso_code(cls, iso_code):
        item = cls.__dict__.get(iso_code)
        if not isinstance(item, CurrencyModel):
            raise ValueError('{} {}'.format(iso_code, ISO_CODE_NOT_FOUND))
        return item
