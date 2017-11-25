from collections import OrderedDict


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
        self.columns = OrderedDict()

    def __getattr__(self, item):
        col = self.columns.get(item)
        if col:
            return col
        return self.__getattribute__(item)

    def __getitem__(self, item):
        return self.rows[item]

    def append(self, row_data):
        row = self.Row(self.headers, row_data)
        self.rows.append(row)
        for x in self.headers:
            new_column = self.Column(x, self.rows)
            self.columns[x] = new_column


class SplitTabloColumn(TabloColumn):

    def __init__(self, name, rows):
        super().__init__(name, rows)
        self.format = Format(align=Align.Left, margin=3)

    @property
    def margin(self):
        return self.format.margin

    @margin.setter
    def margin(self, value):
        self.format.margin = value

    def __str__(self):
        return ''


class SplitTabloRow(TabloRow):

    def __init__(self, headers, row_data):
        super().__init__(headers, row_data)


class SplitTablo(Tablo):

    Column = SplitTabloColumn
    Row = SplitTabloRow

    def __init__(self, headers):
        super().__init__(headers)

    def print(self):
        result = []
        for row in self.rows:
            formatted_row = self.format_row(row)
            result.append(joinrow(formatted_row))
        return result

    def format_row(self, row):
        result = []
        for header_name in self.headers:
            data = getattr(row, header_name)
            column = getattr(self, header_name)
            formatted_data = (data, column.format)
            result.append(formatted_data)
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
