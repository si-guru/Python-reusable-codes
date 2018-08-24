from os import path
from os.path import expanduser
from os.path import realpath
from os.path import dirname
from os.path import basename
from os.path import splitext


def __get_parent_directory__(file_name):
    directory = ""
    try:
        expanded_dir = expanduser(file_name)
        realpath_dir = realpath(expanded_dir)
        directory = dirname(realpath_dir)
    except Exception as ex:
        print(ex)
    return directory

def __get_bot_name__(file_name):
    bot_name = ""
    try:
        file_name = basename(file_name)
        bot_name, extension = splitext(file_name)
    except Exception as ex:
        print(ex)
    return bot_name

def get_string_between(actual, start, end):
    between_string = ""
    try:
        start = actual.index(start) + len(start)
        end = actual.index(end, start)
        between_string = actual[start:end]
    except Exception as ex:
        print(ex)

    return between_string

def get_reverse(value):
    reverse = ""
    try:
        reverse = value[::-1]
    except Exception as ex:
        print(ex)
    return reverse