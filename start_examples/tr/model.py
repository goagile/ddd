

class TRWrapper:

    def __init__(self, config):
        self.pattern_to_search = config.pattern_to_search
        self.pattern_to_replace = config.pattern_to_replace
        self.patterns_to_skip = config.patterns_to_skip

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
