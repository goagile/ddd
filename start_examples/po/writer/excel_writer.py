from openpyxl import Workbook
from openpyxl.styles import PatternFill, colors, Alignment
from openpyxl.utils import get_column_letter

from nilsson.start_examples.po.utils import join_by_new_line


class ExcelWriter:

    @classmethod
    def write(cls, excel_path, msg_collection):
        wb = Workbook()
        ws = wb.get_active_sheet()
        alignment = Alignment(wrapText=True, vertical='top', shrink_to_fit=True)

        for row_index, msg in enumerate(msg_collection, 2):
            if msg.is_plural:
                cell_id = ws.cell(row=row_index, column=1)
                cell_id.alignment = alignment
                cell_id.value = join_by_new_line([msg.id, msg.id_plural])

                cell_en = ws.cell(row=row_index, column=2)
                cell_en.alignment = alignment
                cell_en.value = join_by_new_line(msg.strs)

                cell_paths = ws.cell(row=row_index, column=3)
                cell_paths.alignment = alignment
                cell_paths.value = join_by_new_line(msg.paths)
            else:
                cell_id = ws.cell(row=row_index, column=1)
                cell_id.alignment = alignment
                cell_id.value = msg.id

                cell_en = ws.cell(row=row_index, column=2)
                cell_en.alignment = alignment
                cell_en.value = msg.str

                cell_paths = ws.cell(row=row_index, column=3)
                cell_paths.alignment = alignment
                cell_paths.value = join_by_new_line(msg.paths)

            # ws.row_dimensions[row_index].height = 15

        widths = (25, 30, 80, 20, 40)
        for col, width in enumerate(widths, start=1):
            ws.column_dimensions[get_column_letter(col)].width = width

        wb.save(excel_path)
