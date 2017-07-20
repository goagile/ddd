# from nilsson.start_examples.po.parser.excel_parser import ExcelParser
from start_examples.po.parsers_and_writers.po_parser import PoParser
# from nilsson.start_examples.po.writer.excel_writer import ExcelWriter
from start_examples.po.parsers_and_writers.po_writer import PoWriter

if __name__ == '__main__':
    # path = 'test_simple.po'
    path = 'test_real.po'
    # path = 'test_empty.po'
    path_to_write_po = 'test_write.po'

    msg_collection = PoParser.new().parse_file(path)
    print('\n\nIn:\n'); print(msg_collection)

    PoWriter.new().write_file(path_to_write_po, msg_collection)
    parsed_msg_collection = PoParser.new().parse_file(path_to_write_po)
    print('\n\nParse form test po:\n'); print(parsed_msg_collection)
