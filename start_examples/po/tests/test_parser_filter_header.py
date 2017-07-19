import unittest

from start_examples.po.parsers_and_writers.po_parser import PoParser


class TestParser(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.parser = PoParser.new()

    @unittest.skip('idea')
    def test_parse_path_line(self):
        lines = [
            '# Russian translations for X.\n',
            '# Copyright (C) 2000 ORGANIZATION\n',
            '# This file is distributed under the same license as the X project.\n',
            '# FIRST AUTHOR <EMAIL@ADDRESS>, 2017.\n',
            '#\n',
            'msgid ""\n',
            'msgstr ""\n',
            '"Project-Id-Version: PROJECT VERSION\n"\n',
            '"Report-Msgid-Bugs-To: EMAIL@ADDRESS\n"\n',
            '"POT-Creation-Date: 2000-00-00 18:18+0300\n"\n',
            '"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"\n',
            '"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"\n',
            '"Language: ru\n"\n',
            '"Language-Team: ru <LL@li.org>\n"\n',
            '"Plural-Forms: nplurals=3; plural=(n%10==1 && n%100!=11 ? 0 : n%10>=2 && "\n',
            '"n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)"\n',
            '"MIME-Version: 1.0\n"\n',
            '"Content-Type: text/plain; charset=utf-8\n"\n',
            '"Content-Transfer-Encoding: 8bit\n"\n',
            '"Generated-By: Babel 2.3.4\n"\n',
            '\n',
            '#: ../modules/user/x.js:112 ../modules/user/x.js:300\n',
            'msgid "Box"\n',
            'msgstr "Ящик\n"'
        ]
        expected = [
            '\n'
            '#: ../modules/user/x.js:112 ../modules/user/x.js:300',
            'msgid "Box"',
            'msgstr "Ящик"',
        ]

        result = self.parser.remove_head_lines(lines)

        self.assertEqual(expected, result)
