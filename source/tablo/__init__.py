

class TabloRow:

    def __init__(self, headers, row_data):
        self.headers = headers
        self.__row_data = row_data

    @property
    def data(self):
        return [d for d in self.__row_data]

    def __getattr__(self, item):
        if item not in self.headers and item not in self.__dict__:
            raise InvalidColumnName(item)
        if item in self.headers:
            i = self.headers.index(item)
            return self.__row_data[i]
        return self.__getattribute__(item)

    def __getitem__(self, item):
        return self.__row_data[item]


class InvalidColumnName(Exception):
    pass


class TabloColumn:

    def __init__(self, name, rows):
        self.rows = self.collect_rows(name, rows)

    def collect_rows(self, name, rows):
        result = []
        for row in rows:
            result.append(getattr(row, name))
        return result

    def __getitem__(self, item):
        if len(self.rows) < item:
            raise InvalidRowIndex(item)
        return self.rows[item]


class InvalidRowIndex(Exception):
    pass


class Tablo:

    Column = TabloColumn
    Row = TabloRow

    def __init__(self, headers):
        self.headers = headers
        self.rows = []

    def __getattr__(self, item):
        if item in self.headers:
            return self.Column(item, self.rows)
        return self.__getattribute__(item)

    def __getitem__(self, item):
        return self.rows[item]

    def append(self, row_data):
        row = self.Row(self.headers, row_data)
        self.rows.append(row)


class SplitTabloColumn(TabloColumn):

    def __str__(self):
        return ''


class SplitTabloRow(TabloRow):

    def __init__(self, headers, row_data):
        super().__init__(headers, row_data)

    # def __str__(self):
    #     formatted_sequence = []
    #     for d in self.data:
    #         x = self.__format(d)
    #         formatted_sequence.append(x)
    #     return joinrow(formatted_sequence)
    #
    # def __format(self, data):
    #     format = Format(Align.Left, margin=len(data))
    #     result = (data, format)
    #     return result


class SplitTablo(Tablo):

    Column = SplitTabloColumn
    Row = SplitTabloRow

    def __init__(self, headers):
        super().__init__(headers)
        margins = {k: 3 for k in headers}

    def append(self, row_data):
        row = self.Row(self.headers, row_data)
        self.rows.append(row)

    def print(self):
        result = []
        for r in self.rows:
            self.set_margins(r)
            result.append(r)
        return result

    def set_margins(self, row):
        for k, v in self.margins.items():
            row
        formatted_sequence = []
        for d in self.data:
            x = self.__format(d)
            formatted_sequence.append(x)
        return joinrow(formatted_sequence)

    def __format(self, data):
        format = Format(Align.Left, margin=len(data))
        result = (data, format)
        return result


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
