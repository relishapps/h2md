# -*- coding: utf-8 -*-

from char import Char


class Scanner:
    source = None
    last_index = None
    index = None
    line = None
    column = None

    def __init__(self, source):
        self.source = source
        self.last_index = len(source) - 1
        self.index = 0
        self.line = 0
        self.column = 0

    def get(self):
        if self.index > self.last_index:
            c = "\0"
        else:
            c = self.source[self.index]

        char = Char(c, self.line, self.column, self.index, self.source)

        self.column += 1

        if c != "\0" and self.source[self.index] == "\n":
            self.line += 1
            self.column = 0

        self.index += 1

        return char
