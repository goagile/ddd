import codecs

from start_examples.po.config_po_states import waiting_new_line, command_channel
from start_examples.po.msg_model.msg_collection import MsgCollection
from start_examples.po.parser.po_parser import PoParser
from start_examples.po.state_machine_model.controller import Controller
from start_examples.po.state_machine_model.state_machine import StateMachine

if __name__ == '__main__':
    path = 'test.po'
    with codecs.open(path, "r", "utf-8") as file:
        lines = file.readlines()

    print(''.join(lines))

    po_parser = PoParser(Controller(
        StateMachine(waiting_new_line),
        command_channel,
        MsgCollection()
    ))

    # po_parser.parse_lines(lines)
    #
    # msg_collection = po_parser.msg_collection
    #
    # print(msg_collection)