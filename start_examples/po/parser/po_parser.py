

class PoParser:

    def __init__(self, controller):
        self.controller = controller

    @property
    def msg_collection(self):
        return self.controller.msg_collection

    def parse_lines(self, lines):
        for line in lines:
            if line == '\n':
                self.controller.handle('new_line_finded', line)

            elif line.startswith('#:'):
                self.controller.handle('paths_finded', line)

            elif line.startswith('msgid_plural'):
                self.controller.handle('msgid_plural_finded', line)

            elif line.startswith('msgid'):
                self.controller.handle('msgid_finded', line)

            elif line.startswith('msgstr[0]'):
                self.controller.handle('msgstr_0_finded', line)

            elif line.startswith('msgstr[1]'):
                self.controller.handle('msgstr_1_finded', line)

            elif line.startswith('msgstr[2]'):
                self.controller.handle('msgstr_2_finded', line)

            elif line.startswith('msgstr'):
                self.controller.handle('msgstr_finded', line)

            else:
                raise ValueError('Ошибка чтения po', line)
