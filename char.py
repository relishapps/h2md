# -*- coding: utf-8 -*-


class Char:
    content = None
    index = None
    line = None
    column = None
    source = None

    def __init__(self, content, line, column, index, source):
        self.content = content
        self.line = line
        self.column = column
        self.index = index
        self.source = source

    def __unicode__(self):
        if self.content == " ":
            content = "<space>"
        elif self.content == "\n":
            content = "<newline>"
        elif self.content == "\t":
            content = "<tab>"
        elif self.content == "\0":
            content = "<eof>"
        else:
            content = self.content

        return "%6s %4s    %s" % (self.line, self.column, content)

    def __str__(self):
        return unicode(self).encode('utf-8')
