from start_examples.po.parser.po_parser import PoParser
from start_examples.po.parser.excel_parser import RuEnExcelParser
from start_examples.po.writer.excel_writer import RuEnExcelWriter


if __name__ == '__main__':
    excel_path = 'test_excel.xlsx'
    ru_path = 'test_ru.po'
    en_path = 'test_en.po'

    # WRITE
    # ru_msg_collection = PoParser.new().parse_file(ru_path)
    # en_msg_collection = PoParser.new().parse_file(en_path)
    # # print('\nRU: \n'); print(ru_msg_collection)
    # # print('\nEN: \n'); print(en_msg_collection)
    # RuEnExcelWriter().write(excel_path, ru_msg_collection, en_msg_collection)


    # PARSE
    parse_result = RuEnExcelParser().parse(excel_path)
    print('\nRU: \n'); print(parse_result.ru_msg_collection)
    print('\nEN: \n'); print(parse_result.en_msg_collection)
    print('\nEN: \n'); print(parse_result.new_ru_msg_collection)
    print('\nEN: \n'); print(parse_result.new_en_msg_collection)
