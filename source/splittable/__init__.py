

class SplitTable:

    def __init__(self, headers):
        self.headers = headers
        self.rows = []

    def __getattr__(self, item):
        if item in self.headers:
            return SplitTableColumn(item, self.rows)
        return self.__getattribute__(item)

    def __getitem__(self, item):
        return self.rows[item]

    def append(self, row_data):
        row = SplitTableRow(self.headers, row_data)
        self.rows.append(row)


class SplitTableRow:

    def __init__(self, headers, row_data):
        self.headers = headers
        self.row_data = row_data

    def __getattr__(self, item):
        if item not in self.headers and item not in self.__dict__:
            raise InvalidColumnName(item)
        if item in self.headers:
            i = self.headers.index(item)
            return self.row_data[i]
        return self.__getattribute__(item)


class InvalidColumnName(Exception):
    pass


class SplitTableColumn:

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
