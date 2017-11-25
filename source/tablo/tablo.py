from collections import OrderedDict


ERROR_TEMPLATE = "'{}' {}"
INVALID_ROW_INDEX = 'Invalid row index'
INVALID_COLUMN_NAME = 'Invalid column name'


class TabloRow:

    def __init__(self, headers, row_data):
        self._headers = headers
        self.__row_data = row_data

    @property
    def data(self):
        return [d for d in self.__row_data]

    def __getattr__(self, item):
        if item not in self._headers and item not in self.__dict__:
            raise AttributeError(ERROR_TEMPLATE.format(item, INVALID_COLUMN_NAME))
        if item in self._headers:
            i = self._headers.index(item)
            return self.__row_data[i]
        return self.__getattribute__(item)

    def __getitem__(self, item):
        return self.__row_data[item]


class TabloColumn:

    def __init__(self, name, rows):
        self._rows = self.__collect_rows(name, rows)

    def __collect_rows(self, name, rows):
        return [getattr(row, name) for row in rows]

    def __getitem__(self, item):
        if len(self._rows) < item:
            raise AttributeError(ERROR_TEMPLATE.format(item, INVALID_ROW_INDEX))
        return self._rows[item]


class Tablo:

    _Column = TabloColumn
    _Row = TabloRow

    def __init__(self, headers):
        self._headers = headers
        self._rows = []
        self._columns = OrderedDict()

    def __getattr__(self, item):
        col = self._columns.get(item)
        if col:
            return col
        return self.__getattribute__(item)

    def __getitem__(self, item):
        return self._rows[item]

    def append_row(self, row_data):
        new_row = self._Row(self._headers, row_data)
        self._rows.append(new_row)
        self.__recreate_columns()

    def __recreate_columns(self):
        for h in self._headers:
            new_column = self._Column(h, self._rows)
            self._columns[h] = new_column
