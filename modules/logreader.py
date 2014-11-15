#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ApplicationWeightLogReader:
    def __init__(self):
        print("init class.")

    def read_as_convertable(self, filename):
        file = open(filename, "r", encoding="utf-8")
        first_line = file.readline()
        parser = self._get_parser(first_line)

        return None if parser == "" else  parser.parse(file)
    
    def _get_parser(sef, first_line):
        parser = ""
        if "\"RecStyle\"" in first_line:
            parser = ""
        elif first_line.startswith("日時 ["):
            parser = ""

        return parser
