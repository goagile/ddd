

class TRWrapper:

    def __init__(self, config):
        self.pattern = config.CONST
        self.sub = config.TR
        self.ignore = config.IGNORE

    def wrap(self, text):
        parts = self.pattern.split(text)
        result = [self.find(part) for part in parts]
        return ''.join(result)

    def find(self, text):
        if self.match(text):
            return self.pattern.sub(self.sub, text)
        return text

    def match(self, text):
        return bool(
            self.pattern.match(text)
            and not any(ign.match(text) for ign in self.ignore)
        )
