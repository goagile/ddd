import codecs

# from nilsson.start_examples.po.parser.excel_parser import ExcelParser
from nilsson.start_examples.po.parser.po_parser import PoParser
# from nilsson.start_examples.po.writer.excel_writer import ExcelWriter
from nilsson.start_examples.po.writer.po_writer import PoWriter

if __name__ == '__main__':
    # excel_path = 'text.xlsx'

    path = 'test.po'
    with codecs.open(path, "r", "utf-8") as file:
        lines = file.readlines()

    po_parser = PoParser.new()
    po_parser.parse_lines(lines)
    msg_collection = po_parser.msg_collection
    print('\n\nIn:\n')
    print(msg_collection)

    po_writer = PoWriter.new()
    lines = po_writer.write_lines(msg_collection)
    path_to_write_po = 'test_write.po'
    with codecs.open(path_to_write_po, "w", "utf-8") as file:
        file.write('\n'.join(lines))

    with codecs.open(path_to_write_po, "r", "utf-8") as file:
        lines = file.readlines()
    po_parser = PoParser.new()
    po_parser.parse_lines(lines)
    msg_collection = po_parser.msg_collection
    print('\n\nParse form test po:\n')
    print(msg_collection)

    # ExcelWriter.write(excel_path, msg_collection)
    # result = ExcelParser.parse(excel_path)
    # print('\n\nParsed:\n')
    # print(result)
