from start_examples.po.parser.po_parser import PoParser
from start_examples.po.writer.excel_writer import RuEnExcelWriter
from start_examples.po.writer.po_writer import PoWriter


if __name__ == '__main__':
    excel_path = 'test_excel.xlsx'
    ru_path = 'test_ru.po'
    en_path = 'test_en.po'

    ru_msg_collection = PoParser.new().parse_file(ru_path)
    en_msg_collection = PoParser.new().parse_file(en_path)

    RuEnExcelWriter().write(excel_path, ru_msg_collection, en_msg_collection)
