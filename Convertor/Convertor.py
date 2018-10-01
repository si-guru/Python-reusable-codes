"""
Name        :   Convertor
Usage       :   Convertor is used to convert various python types to
                Other types
Reusability :   -
Author      :   DomainBOTS
Created on  :   08/30/2018
---------------------------------------------------------------------------------
Change Log: Recent Modification in TOP
---------------------------------------------------------------------------------
Date        Modified By     Version              Modification
---------------------------------------------------------------------------------
08/30/2018  DomainBOTS          1.00                 Initial Code
"""
import csv

from .. import LogProvider

logger = LogProvider.Logger
bot_name = logger.__get_bot_name__(__file__)
ipc_object = logger.InterProcessCommunicator(module=bot_name)


class JSON:

    def __init__(self):
        return None


class File_Type:

    __file_object = None

    def __init__(self, file_name, mode='r'):
        self.__file_object = open(file_name, mode)
        return None

    def __del__(self):
        self.__file_object.close()
        return None

    def to_json(self, type='csv', delimiter=','):
        rows = []
        if(type.lower() == 'csv'):
            reader = csv.reader(self.__file_object, delimiter=delimiter)
            for row in reader:
                rows.append(row)
        header = rows[0]
        rows = rows[1:]

        json_array = []
        for row in rows:
            dict_object = {}
            for key, value in enumerate(row):
                key = header[key].strip()
                dict_object[key] = value.strip()
            if(not (dict_object == {})):
                json_array.append(dict_object)

        return json_array
