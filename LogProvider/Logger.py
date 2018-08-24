"""
Name        :   Logger
Usage       :   Allows Logging functionality using python
Reusability :   Completely Reusable
Author      :   AVM-Automation-SGO
Created on  :   06/06/2018
-----------------------------------------------------------------------------
Change Log: Recent Modification in TOP
-----------------------------------------------------------------------------
Date        Mod By  Ver     Modification
-----------------------------------------------------------------------------
08/13/2018  528664  1.11    Modified Code as per PEP8 and pyLint standards
06/06/2018  528664  1.10    Added a new function "write_default_log"
06/05/2018  528664  1.01    Added docstrings to all functions
03/29/2018  528664  1.00    Initial Code
"""

# python Library
import logging
import logging.config
import inspect
import os


class InterProcessCommunicator():
    """InterProcessCommunicator - A customised class which holds basic details
        for inter-process communication
    """
    def __init__(
            self, data=None, status=None, message=None,
            level=None, module=None, success=None
            ):

        self.data = data
        self.message = message
        self.status = status
        self.level = level
        self.success = success
        self.module = module
        return None

    def __str__(self):
        message = ""
        message = message + """InterProcessCommunicator - 
                                Used for communcation between process\n
                                """
        message = message + str("MODULE : " + str(self.module) + "\n")
        return message


# Create own contextual information
class ContextFilter(logging.Filter):
    def filter(self, record):
        record.module = module
        return True


def __initiate_logger(log_object):
    """Initiate Logger will creates context filter and other initiation for logger

    Arguments:
        log_object {InterProcessCommunicator}
            -- log_object is an IPC object which holds basic details for
                interprocess communication

    Returns:
        Logger -- python logger object
    """

    # create logger
    logger = logging.getLogger()
    global module
    module = log_object.module
    log_object.success = True
    # Create contextual filter to add module to the handler
    filter_set = ContextFilter()
    logger.addFilter(filter_set)
    return logger


def write_debug_log(log_object=None, can_log=True):
    """write_debug_log - Writes a debug message into log file

    Keyword Arguments:
        log_object {InterProcessCommunicator}
            -- IPC Object which holds basic communication data
                (default: {None})
        can_log {bool}
            -- Manually set whether to log the message (default: {True})

    Returns:
        [InterProcessCommunicator]
            -- IPC Object which holds basic communication data
    """

    if(can_log):
        try:
            logger = __initiate_logger(log_object)
            logger.debug(str(log_object.message))
        except:
            log_object.success = False
            __write_log_exception()

        finally:
            logging.shutdown()
    else:
        print('Manual log prevention - Activated')
    return log_object


def write_info_log(log_object=None, can_log=True):
    """write_info_log - Writes a info message into log file

    Keyword Arguments:
        log_object {InterProcessCommunicator}
            -- IPC Object which holds basic communication data
                (default: {None})
        can_log {bool}
            -- Manually set whether to log the message (default: {True})

    Returns:
        [InterProcessCommunicator]
            -- IPC Object which holds basic communication data
    """

    if(can_log):
        try:
            logger = __initiate_logger(log_object)
            logger.info(str(log_object.message))
        except:
            log_object.success = False
            __write_log_exception()

        finally:
            logging.shutdown()
    else:
        print('Manual log prevention - Activated')
    return log_object


def write_error_log(log_object=None, can_log=True):
    """write_error_log - Writes a error message into log file

    Keyword Arguments:
        log_object {InterProcessCommunicator}
            -- IPC Object which holds basic communication data
                (default: {None})
        can_log {bool}
            -- Manually set whether to log the message (default: {True})
 
    Returns:
        [InterProcessCommunicator]
            -- IPC Object which holds basic communication data
    """
    if(can_log):
        try:
            logger = __initiate_logger(log_object)
            logger.error(str(log_object.message))
        except:
            log_object.success = False
            __write_log_exception()
        finally:
            logging.shutdown()
    else:
        print('Manual log prevention - Activated')
    return log_object


def write_warning_log(log_object=None, can_log=True):
    """write_warning_log - Writes a warning message into log file

    Keyword Arguments:
        log_object {InterProcessCommunicator}
            -- IPC Object which holds basic communication data
                (default: {None})
        can_log {bool}
            -- Manually set whether to log the message (default: {True})

    Returns:
        [InterProcessCommunicator]
            -- IPC Object which holds basic communication data
    """
    if(can_log):
        try:
            logger = __initiate_logger(log_object)
            logger.warning(str(log_object.message))
        except:
            log_object.success = False
            __write_log_exception()

        finally:
            logging.shutdown()
    else:
        print('Manual log prevention - Activated')
    return log_object


def write_critical_log(log_object=None, can_log=True):
    """write_critical_log - Writes a critical message into log file

    Keyword Arguments:
        log_object {InterProcessCommunicator}
            -- IPC Object which holds basic communication data
                (default: {None})
        can_log {bool}
            -- Manually set whether to log the message (default: {True})

    Returns:
        [InterProcessCommunicator]
            -- IPC Object which holds basic communication data
    """
    if(can_log):
        try:
            logger = __initiate_logger(log_object)
            logger.critical(str(log_object.message))
        except:
            log_object.success = False
            __write_log_exception()
        finally:
            logging.shutdown()
    else:
        print('Manual log prevention - Activated')
    return log_object


def write_default_log(log_object=None, can_log=True):
    """write_default_log - Writes a message into log file, based on given
                            log level

    Keyword Arguments:
        log_object {InterProcessCommunicator}
            -- IPC Object which holds basic communication data
                (default: {None})
        can_log {bool}
            -- Manually set whether to log the message (default: {True})

    Returns:
        [InterProcessCommunicator]
            -- IPC Object which holds basic communication data
    """
    if(can_log):
        try:
            logger = __initiate_logger(log_object)
            error_level = log_object.level.lower()
            message = log_object.message

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

        except:
            log_object.success = False
            __write_log_exception()
        finally:
            logging.shutdown()
    else:
        print('Manual log prevention - Activated')
    return log_object


def __write_log_exception():
    """__write_log_exception - Writes exception log for Logger occurs

    Returns:
        [InterProcessCommunicator]
            -- IPC Object which holds basic communication data
    """

    innerframe = inspect.currentframe()
    outerframes = inspect.getouterframes(innerframe)
    called_function = str(outerframes[1][3])
    log_object = InterProcessCommunicator()
    log_object.module = 'LogProvider'
    log_object.message = 'Unable to load Logger/ Logger not available in '
    log_object.message = log_object.message + called_function
    write_critical_log(log_object)

    return log_object


def __get_parent_directory(file_name):
    expanded_dir = os.path.expanduser(file_name)
    realpath_dir = os.path.realpath(expanded_dir)
    directory = os.path.dirname(realpath_dir)
    return directory


def __CONFIG_FILE_NAME():
    log_path = __get_parent_directory(__file__)
    if(os.path.exists(log_path)):
        return os.path.join(log_path, 'logger.ini')
    else:
        return os.path.join(os.getcwd(), 'logger.ini')


def __get_bot_name__(file_name):
    return os.path.splitext(os.path.basename(file_name))[0]

# Load the configuration file
_CONFIG_FILE_NAME = __CONFIG_FILE_NAME()
logging.config.fileConfig(_CONFIG_FILE_NAME)
module = ''
