

class AlignTemplate:

    def __init__(self, template):
        self.template = template


class Align:
    Left = AlignTemplate('{}{{:{}}}')
    Center = AlignTemplate('{}{{:^{}}}')
    Right = AlignTemplate('{}{{:>{}}}')


class Format:
    def __init__(self, align, margin):
        self.align = align
        self.margin = margin


def joinrow(formatted_sequence, separator='|'):
    result = ''
    for s, format in formatted_sequence:
        template = format.align.template.format(separator, format.margin)
        result += template.format(s)
    return result + separator
