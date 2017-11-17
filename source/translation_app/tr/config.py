import re

from nilsson.start_examples.tr.model import Patterns, TRWrapper


def q(text):
    quotes = r'(?:\'|\")'
    return '({}{}{})'.format(quotes, text, quotes)


tr = r'TR(\1)'
ru = r'А-Яа-я'
special_symbols = r'- :_;.,?!'
ru_and_symbols = q(r'[{}{}]+'.format(special_symbols, ru))


patterns = Patterns(
    to_search=ru_and_symbols,
    to_replace=tr
)
patterns.add_to_skip(q(r'[{}]+'.format(special_symbols)))
patterns.add_to_skip(q(r', '))


wrapper = TRWrapper(patterns)
