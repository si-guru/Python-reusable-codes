"""
This python script log the message in the generic place based upon the setting in configuration file.
Here python default logging utility used.
Author:AVM-AUTOMATION(Cognizant)
Date:12/19/2017
Version:1.0
Environment: Python 2.7.12
"""
# This library is used to work with logger and logger configuration file
import logging
import logging.config
import os
import sys

pathEnvVar="PYTHONLOG"
notLog=False

'''checkLogPath=os.environ.has_key(pathEnvVar)
if checkLogPath == True :
    logPath=os.environ.get(pathEnvVar) + "\\Logger.ini"
    # Load the configuration file 
    logging.config.fileConfig(logPath)
else :
    notLog=True'''

#Modify the configuration file path accordingly

moduleDirectory =  os.path.dirname(os.path.realpath(__file__))
logPath = moduleDirectory + '\\Logger.ini'

# logPath=r'C:\Users\445781\Documents\Python\Temporary-Version\Logger.ini'

#Load the configuration path
logging.config.fileConfig(logPath)

name=''

#Create own contextual information 
class ContextFilter(logging.Filter):
    def filter(self, record):
        record.botName = name
        return True


# This function will log the message to the file
def log_message(botName,message,errorLevel):
    if notLog == False :
        try:
            # create logger
            logger = logging.getLogger()
            global name
            name=botName
            #Create contextual filter to add botname to the handler
            filterSet=ContextFilter()
            logger.addFilter(filterSet)
            if(errorLevel=='debug'):
                logger.debug(str(message))
            elif(errorLevel == 'info'):
                logger.info(str(message))
            elif(errorLevel == 'warn'):
                logger.warn(str(message))
            elif(errorLevel == 'error'):
                logger.error(str(message))   
            elif(errorLevel == 'critical'):
                logger.critical(str(message))
            else:
                logger.critical('Unable to find the error level described')
        except Exception as e:
            print('Logging not possible')
        finally:
            logging.shutdown()
    else:
        print('Python logging environment variable not set. So logging is not possible')








