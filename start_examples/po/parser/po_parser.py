

class PoParser:

    def __init__(self, controller):
        self.controller = controller

    def parse_lines(self, lines):
        for line in lines:
            if line == '\n':
                self.controller.handle('new_line_finded', line)
            elif line.startswith('#:'):
                self.controller.handle('paths_finded', line)
            elif line.startswith('msgid'):
                self.controller.handle('msgid_finded', line)
            elif line.startswith('msgstr'):
                self.controller.handle('msgstr_finded', line)
            else:
                raise ValueError('Ошибка чтения po', line)
