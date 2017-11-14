import re


class TRWrapper:

    def __init__(self, config):
        self.pattern_to_search = re.compile(config.to_search)
        self.pattern_to_replace = config.to_replace
        self.patterns_to_skip = config.to_skip

    def wrap(self, text):
        parts = self.pattern_to_search.split(text)
        result = [self.find(part) for part in parts]
        return ''.join(result)

    def find(self, text):
        if self.match(text):
            return self.pattern_to_search.sub(self.pattern_to_replace, text)
        return text

    def match(self, text):
        return bool(
            self.pattern_to_search.match(text)
            and not any(ign.match(text) for ign in self.patterns_to_skip)
        )


class Patterns:

    def __init__(self, to_search, to_replace):
        self.to_search = to_search
        self.to_replace = to_replace
        self.__to_skip = []

    @property
    def to_skip(self):
        return self.__to_skip

    def add_to_skip(self, pattern):
        compiled = re.compile(pattern)
        self.to_skip.append(compiled)
