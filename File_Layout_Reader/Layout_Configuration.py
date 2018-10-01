"""
Name        :   Layout_Configuration
Usage       :   
Reusability :   -
Author      :   DomainBOTS
Created on  :   08/17/2018
---------------------------------------------------------------------------------
Change Log: Recent Modification in TOP
---------------------------------------------------------------------------------
Date        Modified By     Version              Modification
---------------------------------------------------------------------------------
08/17/2018  DomainBOTS          1.00                 Initial Code
"""

import os
import json
import configparser
# from configparser import options

# Custom Modules
from .. import Globals
try:
    if(not Globals.setting):
        Globals.start()

    setting = Globals.setting
    logger = setting['Logger']
    ipc_object = setting['IPC_Object']
except Exception as ex:
    print("Exception when loading globals")


class Layout_Constants:
    LAYOUT_META_HEADER = "Segments"

    LAYOUT_BODY = "Basic"


class Layout_Configuration:

    layout_array = None

    def __init__(self):
        return None

    def write_object_to_file(self, py_object, file_path):
        with open(file_path, 'w') as jsonFile:
            json.dump(py_object, jsonFile, indent = 1)
        return None

    def store_layout_as_object(self, column_values, config_parser):
        column_names = ""
        label = column_values[0]
        dictobject = {}
        try:
            column_names = config_parser.get(label, Layout_Constants.LAYOUT_BODY)
            column_names = column_names.split(',')
            if(len(column_names) != len(column_values)):
                ipc_object.message = str("store_layout_as_object"
                + ", Length Error for " + column_values[0])
                logger.write_error_log(ipc_object)
            else:
                for index, column_value in enumerate(column_values):
                    dictobject[column_names[index]] = column_value.strip()
            # dictobject = {dictobject['label']: dictobject}

        except Exception as ex:
            ipc_object.message = ("Store_layout_as_object" + str(ex))
            logger.write_error_log(ipc_object)
        return dictobject

    def generate_layout_file_array(self, layout_file, config_file):
        is_valid = (
            os.path.exists(config_file) and 
            os.path.exists(layout_file)
            )
        json_array = {}
   
        if (is_valid):
            __config_parser = configparser.RawConfigParser()
            __config_parser.read(config_file)

            # Reads the given file and removes CRLF, then splits using '~'
            with open(layout_file, 'rb') as file_reader:
                layout_line = file_reader.readline().decode('utf-8')
                layout_lines = ""
                while(layout_line != ""):
                    layout_line = file_reader.readline().decode('utf-8')
                    layout_line = layout_line.strip("\n").strip("\r")
                    layout_lines = layout_lines + layout_line
                layout_lines = layout_lines.split("~")

            for current_line in layout_lines:
                column_values = current_line
                column_values = column_values.strip('~\r\n').split('*')
                json_object = self.store_layout_as_object(column_values, __config_parser)
                try:
                    # print(json_object)
                    label = json_object['label'] or "Dummy"
                except:
                    label = ""
                json_array[label] = json_object
        return json_array