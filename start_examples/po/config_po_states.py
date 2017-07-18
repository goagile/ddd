from nilsson.start_examples.po.state_machine_model.commands import (
    ParseMsgPath,
    ParseMsgId,
    ParseMsgStr,
    ParseMsgIdPlural,
    ParseMsgStr0,
    ParseMsgStr1,
    ParseMsgStr2,
    CreateCurrentMsg
)
from nilsson.start_examples.po.state_machine_model.event import Event
from nilsson.start_examples.po.state_machine_model.state import State


waiting_new_line = State('waiting_new_line')
new_line_finded = Event('new_line_finded')


waiting_paths = State('waiting_paths')
paths_finded = Event('paths_finded')


waiting_msgid = State('waiting_msgid')
msgid_finded = Event('msgid_finded')
msgid_plural_finded = Event('msgid_plural_finded')


waiting_msgstr = State('waiting_msgstr')
msgstr_finded = Event('msgstr_finded')


waiting_msgstr_0 = State('waiting_msgstr_0')
msgstr_0_finded = Event('msgstr_0_finded')

waiting_msgstr_1 = State('waiting_msgstr_1')
msgstr_1_finded = Event('msgstr_1_finded')


waiting_msgstr_2 = State('waiting_msgstr_2')
msgstr_2_finded = Event('msgstr_2_finded')


waiting_new_line.add_transition(target=waiting_paths, event=new_line_finded, commands=['create_current_msg'])

waiting_paths.add_transition(target=waiting_msgid, event=paths_finded, commands=['parse_path'])

waiting_msgid.add_transition(target=waiting_msgid, event=paths_finded, commands=['parse_path'])
waiting_msgid.add_transition(target=waiting_msgstr, event=msgid_finded, commands=['parse_msgid'])

waiting_msgstr.add_transition(target=waiting_paths, event=msgstr_finded, commands=[
    'parse_msgstr', 'create_current_msg'
])
waiting_msgstr.add_transition(target=waiting_msgstr_0, event=msgid_plural_finded, commands=['parse_msgid_plural'])

waiting_msgstr_0.add_transition(target=waiting_msgstr_1, event=msgstr_0_finded, commands=['parse_msgstr_0'])

waiting_msgstr_1.add_transition(target=waiting_paths, event=new_line_finded, commands=['create_current_msg'])
waiting_msgstr_1.add_transition(target=waiting_msgstr_2, event=msgstr_1_finded, commands=['parse_msgstr_1'])


waiting_msgstr_2.add_transition(target=waiting_paths, event=new_line_finded, commands=['create_current_msg'])
waiting_msgstr_2.add_transition(target=waiting_new_line, event=msgstr_2_finded, commands=['parse_msgstr_2'])


command_channel = {
    'parse_path': ParseMsgPath('parse_path'),
    'parse_msgid': ParseMsgId('parse_msgid'),
    'parse_msgstr': ParseMsgStr('parse_msgstr'),
    'parse_msgid_plural': ParseMsgIdPlural('parse_msgid_plural'),
    'parse_msgstr_0': ParseMsgStr0('parse_msgstr_0'),
    'parse_msgstr_1': ParseMsgStr1('parse_msgstr_1'),
    'parse_msgstr_2': ParseMsgStr2('parse_msgstr_2'),
    'create_current_msg': CreateCurrentMsg('create_current_msg')
}
