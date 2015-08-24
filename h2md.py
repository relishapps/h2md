#!/usr/bin/python
# -*- coding: utf-8 -*-

from scanner import Scanner


f = open('RMLStarReceiptPrinter.h', 'r')

source = f.read()

scanner = Scanner(source)

char = scanner.get()

while (True):
    print char

    if char.content == "\0":
        break

    char = scanner.get()
