import re

from nilsson.start_examples.tr.model import Patterns, TRWrapper


def quotes(text):
    q = r'(?:\'|\")'
    return '({}{}{})'.format(q, text, q)


special_symbols = r'- :_;.,?!'
tr = r'TR(\1)'
ru = r'А-Яа-я'

patterns = Patterns()
patterns.to_search = re.compile(quotes(r'[' + special_symbols + ru + ']+'))
patterns.to_replace = r'TR(\1)'
patterns.add_to_skip(pattern=re.compile(quotes('[' + special_symbols + ']+')))
patterns.add_to_skip(pattern=re.compile(quotes(', ')))


wrapper = TRWrapper(patterns)
