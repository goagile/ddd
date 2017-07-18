from openpyxl import load_workbook

from start_examples.po.msg_model.msg_collection import MsgCollection


class ExcelParser:

    @classmethod
    def parse(cls, excel_path):
        wb = load_workbook(excel_path)
        ws = wb.get_active_sheet()

        result = MsgCollection()

        for row in ws.rows:
            id_, msgstrs, paths = row[0].value, row[1].value, row[2].value
            if not row[0].value:
                continue
            if cls.is_plural(id_) or cls.is_plural(msgstrs):
                ids = cls.split_by_new_line(id_)
                result.add_msg_plural(
                    id=ids[0], id_plural=ids[1], strs=cls.split_by_new_line(msgstrs), paths=cls.split_by_new_line(paths)
                )
            else:
                result.add_msg(id=id_, str=msgstrs, paths=cls.split_by_new_line(paths))

        return result

    @classmethod
    def split_by_new_line(cls, str):
        return str.split('\n')

    @classmethod
    def is_plural(cls, value):
        return bool(len(value.split('\n')) > 1)
