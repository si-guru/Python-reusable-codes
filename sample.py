from DB_Interface import Sql_db_interface as sql_db
from LogProvider import Logger as logger
from Generic import Constants as const

import os


def main():
    parent_directory = logger.__get_parent_directory(__file__)
    file_name = const.CONFIG_FILE_NAME + const.CONFIG_FILE_EXTENTION
    file_name = os.path.join(parent_directory, "DB_Interface", file_name)
    db = sql_db.Database(file_name)
    print(db)

main()