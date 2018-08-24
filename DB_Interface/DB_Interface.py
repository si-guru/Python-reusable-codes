"""
Name        :   DB_Interface
Usage       :   Allows access to database and provides functionalities within the database
Reusability :   Completely Reusable
Author      :   AVM-Automation-SGO
Created on  :   06/06/2018
--------------------------------------------------------------
Change Log:
--------------------------------------------------------------
Date        Modified By     Version              Modification
--------------------------------------------------------------
06/06/2018  528664          1.0                 Initial Code
"""

# Import Section

# Inbuilt Library
import configparser
import base64
import os
import sys
import json

# Third-party Library
import pyodbc
import pandas

# Custom Library
import Constants as const
from LogProvider import Logger as logger

# Constant Variables

CONFIG_META_HEADER = "Database"
CONFIG_META_DATA_DRIVER = "driverName"
CONFIG_META_DATA_SERVER = "serverName"
CONFIG_META_DATA_DB_USERNAME = "userName"
CONFIG_META_DATA_DB_PASSWORD = "password"
CONFIG_META_DATA_DOMAIN = "domain"

ERROR_DB_CONNECTION = "Error while connecting to database"
ERROR_CON_STRING = "Error generating connection string, Please initiate the class properly"

INFO_DB_CONNECT_SUCCESS = "Database connection successfull.."
INFO_BOT_LOAD_SUCCESS = "Bot loaded successfully"
INFO_BOT_END_SUCCESS = "Bot Ended successfully"

class Database:

    # private variables
    __connection = None
    __database_server = None
    __database_type = None
    __database_username = None
    __database_password = None
    __database_domain = None
    __config_parser = None
    __ipc_object = None

    def __init__(self, config_file):
        
        self.__ipc_object           = globals()['ipc_object']

        self.__config_parser        = configparser.RawConfigParser()
        self.__config_parser.read(config_file)
        self.__database_server      = self.__config_parser.get(const.CONFIG_META_HEADER, const.CONFIG_META_DATA_DB_HOSTNAME)
        self.__database_type        = self.__config_parser.get(const.CONFIG_META_HEADER, const.CONFIG_META_DATA_DRIVER)
        self.__database_username    = self.__config_parser.get(const.CONFIG_META_HEADER, const.CONFIG_META_DATA_DB_USERNAME)
        password                    = self.__config_parser.get(const.CONFIG_META_HEADER, const.CONFIG_META_DATA_DB_PASSWORD)
        self.__database_password    = (base64.b64decode(password)).decode()
        self.__database_domain      = self.__config_parser.get(const.CONFIG_META_HEADER, const.CONFIG_META_DATA_HOST_DOMAIN)
        # print(self.__database_server)
        self.__connect_database()
        return None

    def get_connection(self):
        if(not self.__connection):
            self.__connect_database()
        return self.__connection

    def set_connection(self, connection):
        self.__ipc_object.message = INFO_DB_CONNECT_SUCCESS
        self.__connection = connection
        print(self.__ipc_object)
        logger.write_info_log(self.__ipc_object)

    def __connect_database(self):

        try:
            connection_string = "Driver={" + self.__database_type + "};Server=" + self.__database_server + "."
            connection_string = connection_string + self.__database_domain + ";UID=" + self.__database_username
            connection_string = connection_string + ";PWD=" + self.__database_password
        except Exception as ex:
            print(ex)
            self.__ipc_object.messge = ERROR_CON_STRING + " - " + str(ex)
            logger.write_error_log(self.__ipc_object)
            return False

        print(connection_string)

        try:
            connection = pyodbc.connect(connection_string)
        except Exception as ex:
            print(ex)
            self.__ipc_object.messge = ERROR_DB_CONNECTION + " - " + str(ex)
            logger.write_error_log(self.__ipc_object)
            return False

        self.set_connection(connection)
        return True

    def execute_query(self, query):
        
        try:
            if(not self.__connection):
                return False
            result = pandas.read_sql_query(query, self.__connection)
        except Exception as ex:
            print(ex)
            self.__ipc_object.messge = ERROR_DB_CONNECTION + " - " + str(ex)
            logger.write_error_log(self.__ipc_object)
            return False
        print(result.to_json())


def main():
    
    # Initiating Logger
    module = logger.__get_bot_name__(__file__)
    ipc_object = logger.InterProcessCommunicator(module= module)
    
    # Globalized IPC object
    globals()['ipc_object'] = ipc_object
    
    ipc_object.message = INFO_BOT_LOAD_SUCCESS
    logger.write_info_log(ipc_object)

    # Connection to DB
    db = Database("Database.ini")
    query = """
    SELECT TOP 1000 [User_Id]
      ,[First_Name]
      ,[Last_Name]
      ,[Role]
      ,[Status]
    FROM [Education].[dbo].[User_Details] 
    """
    result = db.execute_query(query)
    print(result)
    ipc_object.message = INFO_BOT_END_SUCCESS
    logger.write_info_log(ipc_object)
  


if __name__ == "__main__":

    main()