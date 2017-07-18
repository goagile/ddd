import codecs

from start_examples.po.parser.po_parser import PoParser


if __name__ == '__main__':
    path = 'test.po'
    with codecs.open(path, "r", "utf-8") as file:
        lines = file.readlines()

    po_parser = PoParser.new()

    po_parser.parse_lines(lines)

    msg_collection = po_parser.msg_collection

    print(msg_collection)

    # for m in msg_collection.msgs:
    #     print(m)