from start_examples.po.parser.po_parser import PoParser
from start_examples.po.writer.po_writer import PoWriter


if __name__ == '__main__':
    ru = 'test_ru.po'
    en = 'test_en.po'

    ru_collection = PoParser.new().parse_file(ru)
    en_collection = PoParser.new().parse_file(en)
    print('\n\nRU:\n'); print(ru_collection)

    print('\n\nEN:\n'); print(en_collection)
