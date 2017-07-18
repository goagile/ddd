import codecs

from start_examples.po.parser.excel_parser import ExcelParser
from start_examples.po.parser.po_parser import PoParser
from start_examples.po.writer.excel_writer import ExcelWriter

if __name__ == '__main__':
    excel_path = 'text.xlsx'
    path = 'test.po'
    with codecs.open(path, "r", "utf-8") as file:
        lines = file.readlines()

    po_parser = PoParser.new()

    po_parser.parse_lines(lines)

    msg_collection = po_parser.msg_collection

    print('\n\nIn:\n')
    print(msg_collection)

    ExcelWriter.write(excel_path, msg_collection)

    result = ExcelParser.parse(excel_path)

    print('\n\nParsed:\n')
    print(result)