from openpyxl import load_workbook

from start_examples.po.msg_model.msg_collection import MsgCollection


class RuEnExcelParser:

    @classmethod
    def parse(cls, excel_path):
        wb = load_workbook(excel_path)
        ws = wb.get_active_sheet()

        ru_msg_collection = MsgCollection()
        en_msg_collection = MsgCollection()
        new_ru_msg_collection = MsgCollection()
        new_en_msg_collection = MsgCollection()

        for row in ws.iter_rows(min_row=2):
            cls.__parse_to(ru_msg_collection, row, str_col=1)
            cls.__parse_to(en_msg_collection, row, str_col=2)

        return ru_msg_collection, en_msg_collection

    @classmethod
    def __parse_to(cls, en_msg_collection, row, id_col=0, str_col=1, path_col=6):
        id_, en = row[id_col].value, row[str_col].value
        paths = cls.__split_by_new_line(row[path_col].value)
        if cls.__is_plural(id_, en):
            ids = cls.__split_by_new_line(id_)
            en_msg_collection.add_msg_plural(*ids, strs=cls.__split_by_new_line(en), paths=paths)
        else:
            en_msg_collection.add_msg(id=id_, str=en, paths=paths)

    @classmethod
    def __split_by_new_line(cls, str):
        if str is None:
            return ''
        return str.split('\n')

    @classmethod
    def __is_plural(cls, id_, str):
        return bool(cls.__has_plural_values(id_) or cls.__has_plural_values(str))

    @classmethod
    def __has_plural_values(cls, value):
        if value is None:
            return False
        return bool(len(value.split('\n')) > 1)
