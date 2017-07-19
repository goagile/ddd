import codecs

# from nilsson.start_examples.po.parser.excel_parser import ExcelParser
from nilsson.start_examples.po.parser.po_parser import PoParser
# from nilsson.start_examples.po.writer.excel_writer import ExcelWriter
from nilsson.start_examples.po.writer.po_writer import PoWriter

if __name__ == '__main__':
    path = 'test.po'
    path_to_write_po = 'test_write.po'
    # excel_path = 'text.xlsx'

    msg_collection = PoParser.new().parse_file(path)
    print('\n\nIn:\n'); print(msg_collection)

    PoWriter.new().write_file(path_to_write_po, msg_collection)
    parsed_msg_collection = PoParser.new().parse_file(path_to_write_po)
    print('\n\nParse form test po:\n'); print(parsed_msg_collection)

    # ExcelWriter.write(excel_path, msg_collection)
    # result = ExcelParser.parse(excel_path)
    # print('\n\nParsed:\n'); print(result)