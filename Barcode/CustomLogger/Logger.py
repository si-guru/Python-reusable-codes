"""
This python script log the message in the generic place based upon the setting in configuration file.
Here python default logging utility used.
Author:AVM-AUTOMATION(Cognizant)
Date:28/02/2018
Version:2.0
Environment: Python 3.6.4
"""
# This library is used to work with logger and logger configuration file
import logging
import logging.config
import os
import platform

CONFIGURATION_FILE_NAME = "Logger.ini"

if platform.system() is 'Windows':
    backslash = "\\"
else:
    backslash = "//"

logPath = os.path.split(os.path.abspath(__file__))[0] + backslash + CONFIGURATION_FILE_NAME
if not os.path.exists(logPath):
    logPath = os.getcwd() + backslash + CONFIGURATION_FILE_NAME

# Load the configuration file
logging.config.fileConfig(logPath)

name = ''


# Create own contextual information
class ContextFilter(logging.Filter):
    def filter(self, record):
        #record.botname = name
        record.module = name
        return True


# This function will log the message to the file
def log_message(botname, message, error_level, not_log=False):
    if not not_log:
        try:
            # create logger
            logger = logging.getLogger()
            global name
            name = botname
            error_level = error_level.lower()
            # Create contextual filter to add botname to the handler
            filter_set = ContextFilter()
            logger.addFilter(filter_set)
            if error_level == 'debug':
                logger.debug(str(message))
            elif error_level == 'info':
                logger.info(str(message))
            elif error_level == 'warn':
                logger.warning(str(message))
            elif error_level == 'error':
                logger.error(str(message))
            elif error_level == 'critical':
                logger.critical(str(message))
            else:
                logger.critical('Unable to find the error level described')
        except Exception as error:
            print('Logging not possible' + str(error))
        finally:
            logging.shutdown()
    else:
        print('Warning.User manually suppressed logger')
