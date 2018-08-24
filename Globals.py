from .LogProvider import Logger
from .DB_Interface import Constants


def start():
    global setting
    setting = {
        "Logger": Logger,
        "DB_Constants": Constants
    }
