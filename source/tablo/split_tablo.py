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

    def centred(self):
        self.format.align = Align.Center


class SplitTablo(Tablo):

    Column = SplitTabloColumn

    def __init__(self, headers):
        super().__init__(headers)

    def print(self):
        for row in self.formatted_rows():
            print(joinrow(row))

    def formatted_rows(self):
        return [self.format_row(row) for row in self.rows]

    def format_row(self, row):
        return [self.format_data(row, h) for h in self.headers]

    def format_data(self, row, h):
        data = getattr(row, h)
        column = getattr(self, h)
        return (data, column.format)
