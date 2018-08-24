"""
Name        :   readConfiguration
Usage       :   Reads SMTP configuration details from XML file
Reusability :   Completely Reusable
Author      :   AVM-Automation-SGO
Created on  :   08/13/2018
------------------------------------------------------------------------------
Change Log: Recent Modification in TOP
------------------------------------------------------------------------------
Date        Modified By     Version              Modification
------------------------------------------------------------------------------
08/13/2018  528664          1.00                 Initial Code
"""

# Python modules
import os
import xml.etree.ElementTree as ET
import sys
import smtplib
import string
from datetime import datetime

# Custom Modules
from ..Globals import Logger


class Configuration:

    smtp_server = ""

    def __init__(self, configFilepath):
        print(configFilepath)
        tree = ET.parse(configFilepath)
        root = tree.getroot()
        self.smtp_server = root.find('SmtpServer').text
        return None


def main():
    config_object = Configuration("")
    return None


if __name__ == "__main__":
    main()