#!/usr/bin/python3
'''Module for read_file method.'''


def read_file(filename=""):
    '''Method for reading from file.'''
    with open(filename, "r") as f:
        text = f.read()
        print(text, end="")
    f.close()
