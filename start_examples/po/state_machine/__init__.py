from nilsson.start_examples.po.state_machine.model import State, Event


waiting_new_line = State('waiting_new_line')
new_line_finded = Event('new_line_finded')
waiting_new_line.add_command('print')

waiting_paths = State('waiting_paths')
paths_finded = Event('paths_finded')
waiting_new_line.add_command('print')

waiting_msgid = State('waiting_msgid')
msgid_finded = Event('msgid_finded')
waiting_new_line.add_command('print')

waiting_msgstr = State('waiting_msgstr')
msgstr_finded = Event('msgstr_finded')
waiting_new_line.add_command('print')

waiting_new_line.add_transition(target=waiting_paths, event=new_line_finded)
waiting_paths.add_transition(target=waiting_msgid, event=paths_finded)
waiting_msgid.add_transition(target=waiting_msgstr, event=msgid_finded)
waiting_msgstr.add_transition(target=waiting_new_line, event=msgstr_finded)
