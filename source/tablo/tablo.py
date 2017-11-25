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


class InvalidColumnName(Exception):
    pass


class InvalidRowIndex(Exception):
    pass
