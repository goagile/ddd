from tablo.split_tablo_format import Align, Format, joinrow
from tablo.tablo import TabloColumn, Tablo


class SplitTabloColumn(TabloColumn):

    def __init__(self, name, rows):
        super().__init__(name, rows)
        margin = self.max_margin(self.rows)
        self.format = Format(Align.Left, margin)

    @property
    def margin(self):
        return self.format.margin

    @margin.setter
    def margin(self, value):
        self.format.margin = value

    def max_margin(self, rows):
        return max(len(r) for r in rows)


class SplitTablo(Tablo):

    Column = SplitTabloColumn

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
