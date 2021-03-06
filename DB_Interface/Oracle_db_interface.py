import configparser
import base64
import os
import cx_Oracle as db_interface

from .. import Globals

try:
    setting = Globals.setting
except Exception as ex:
    Globals.start()
    setting = Globals.setting

logger = setting['Logger']
ipc_object = Globals.get_ipc_object(__file__)
convertor = setting['Convertor']

from . import Constants as db_constants

class Database:
    """Database Class provides all the basic functionality of an Oracle Database.
        Has the Following functions:
        -   set_database_connection
        -   get_database_connection
        -   set_cursor
        -   get_cursor
        -   set_ipc_object
        -   get_ipc_object
        -   connect_database
        -   disconnect_database
        -   execute_query
        -   call_procedure

    """

    # Private variables
    __database_username = None
    __database_password = None
    __database_hostname = None
    __database_port = None
    __database_name = None
    __host_domain = None
    __database_dsn = None

    __database_connection = None
    __cursor = None
    __config_parser = None
    __ipc_object = None

    def __init__(self, config_file=None):
        if(config_file):
            self.__config_parser = configparser.RawConfigParser()
            self.__config_parser.read(config_file)
            self.__database_hostname = self.__config_parser.get(
                    db_constants.CONFIG_META_HEADER_ORACLE,
                    db_constants.CONFIG_META_DATA_DB_HOSTNAME
                    )
            self.__database_username = self.__config_parser.get(
                    db_constants.CONFIG_META_HEADER_ORACLE,
                    db_constants.CONFIG_META_DATA_DB_USERNAME
                    )
            password = self.__config_parser.get(
                    db_constants.CONFIG_META_HEADER_ORACLE,
                    db_constants.CONFIG_META_DATA_DB_PASSWORD
                    )
            try:
                self.__database_password = (base64.b32decode(password)).decode()
            except:
                self.__database_password = password
            self.__database_port = self.__config_parser.get(
                    db_constants.CONFIG_META_HEADER_ORACLE,
                    db_constants.CONFIG_META_DATA_DB_PORT
                    )
            self.__database_name = self.__config_parser.get(
                    db_constants.CONFIG_META_HEADER_ORACLE,
                    db_constants.CONFIG_META_DATA_DB_NAME
                    )
            self.__host_domain = self.__config_parser.get(
                    db_constants.CONFIG_META_HEADER_ORACLE,
                    db_constants.CONFIG_META_DATA_HOST_DOMAIN
                    )
            self.__database_dsn = db_interface.makedsn(
                    self.__database_hostname, self.__database_port,
                    self.__database_name
                    )

            self.connect_database()
        self.set_ipc_object(ipc_object)
        return None

    def set_database_username(self, username):
        self.__database_username = username

    def get_database_username(self):
        return self.__database_username

    def set_database_password(self, password):
        try:
            self.__database_password = (base64.b32decode(password)).decode()
        except:
            self.__database_password = password

    def get_database_password(self):
        return self.__database_password

    def set_database_hostname(self, hostname):
        self.__database_hostname = hostname

    def get_database_hostname(self):
        return self.__database_hostname

    def set_database_port(self, database_port):
        self.__database_port = database_port
    
    def get_database_port(self):
        return self.__database_port

    def set_database_name(self, database_name):
        self.__database_name = database_name

    def get_database_name(self):
        return self.__database_name

    def set_host_domain(self, host_domain):
        self.__host_domain = host_domain

    def get_host_domain(self):
        return self.__host_domain

    def set_database_dsn(self, database_dsn):
        self.__database_dsn = database_dsn

    def get_database_dsn(self):
        return self.__database_dsn

    def set_database_connection(self, connection):
        self.__database_connection = connection

    def get_database_connection(self):
        if(not self.__database_connection):
            self.connect_database()
        return self.__database_connection

    def set_cursor(self, cursor):
        self.__cursor = cursor

    def get_cursor(self):
        return self.__cursor

    def set_ipc_object(self, ipc_object):
        self.__ipc_object = ipc_object

    def get_ipc_object(self):
        return self.__ipc_object

    def connect_database(self):
        try:
            print(self.__database_password)
            self.__database_dsn = db_interface.makedsn(
                    self.__database_hostname, self.__database_port,
                    self.__database_name
                    )
            connection = db_interface.connect(
                    self.__database_username, self.__database_password,
                    self.__database_dsn
                    )
            self.set_database_connection(connection)
            cursor = self.__database_connection.cursor()
            self.set_cursor(cursor)
        except Exception as ex:
            print(ex)

    def disconnect_database(self):
        try:
            self.__database_connection.close()
        except Exception as ex:
            print(ex)

    def execute_query(self, query):
        try:
            self.__cursor.execute(query)
        except Exception as ex:
            print(ex)
        return self.__cursor

    def call_procedure(self, procedure, arguments):
        result_set = None
        try:
            result_set = self.__cursor.callproc(procedure, arguments)
        except Exception as ex:
            print(ex)
        return result_set

    def run_query_from_file(self, file_name=None, proc_name=None,
        arguments=None):
        parent_directory = logger.__get_parent_directory(__file__)
        file_name = os.path.join(parent_directory, file_name)

        try:
            result = False

            if(file_name):
                sql_string = ""

                with open(file_name, "r") as file_object:
                    sql_string = file_object.read()

                self.execute_query(sql_string)
                self.__database_connection.commit()
            if(proc_name):
                result = self.call_procedure(proc_name, arguments)
                self.__database_connection.commit()
            if(file_name and proc_name):
                sql_string = "DROP PROCEDURE " + str(proc_name)
                self.execute_query(sql_string)
                self.__database_connection.commit()
            return result
        except Exception as ex:
            self.__database_connection.rollback()
            print(ex)
            return False


def main():
    print("Called as a Main Function - Will Exit !!!")
    
if __name__ == "__main__":
    main()