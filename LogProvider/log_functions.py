
# python Library
import logging
import logging.config
import inspect
import os

from .IPC import InterProcessCommunicator


class logger:

    # __config_file = self.__CONFIG_FILE_NAME()

    def __init__(self, config_file=None):
        if(not config_file):
            config_file = self.__CONFIG_FILE_NAME()
        self.config_logger_from_file(config_file)
        return None

    @DeprecationWarning
    def __initiate_logger(self, ipc_object):
        """Initiate Logger will creates context filter and other initiation for logger

        Arguments:
            ipc_object {InterProcessCommunicator}
                -- ipc_object is an IPC object which holds basic details for
                    interprocess communication

        Returns:
            Logger -- python logger object
        """

        # create logger
        logger = logging.getLogger()
        global module
        module = ipc_object.module
        ipc_object.success = True
        # Create contextual filter to add module to the handler
        filter_set = ContextFilter()
        logger.addFilter(filter_set)
        return logger

    def write_debug_log(self, ipc_object=None, can_log=True):
        """write_debug_log - Writes a debug message into log file

        Keyword Arguments:
            ipc_object {InterProcessCommunicator}
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
                if ipc_object.data:
                    ipc_object.data['method_name'] = self.get_called_function_name()
                    ipc_object.message = "{ipc_object.module} | " + ipc_object.message
                    ipc_object.message = ipc_object.message.format(ipc_object=ipc_object)
                logger = logging.getLogger()
                logger.debug(str(ipc_object.message))
            except Exception as ex:
                print("Exception : " + str(ex))
                # print(ipc_object.message)
                ipc_object.success = False
                self.__write_log_exception()

            finally:
                logging.shutdown()
        else:
            print('Manual log prevention - Activated')
        return ipc_object

    def write_info_log(self, ipc_object=None, can_log=True):
        """write_info_log - Writes a info message into log file

        Keyword Arguments:
            ipc_object {InterProcessCommunicator}
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
                if ipc_object.data:
                    ipc_object.data['method_name'] = self.get_called_function_name()
                    ipc_object.message = "{ipc_object.module} | " + ipc_object.message
                    ipc_object.message = ipc_object.message.format(ipc_object=ipc_object)
                logger = logging.getLogger()
                logger.info(str(ipc_object.message))
            except:
                ipc_object.success = False
                self.__write_log_exception()

            finally:
                logging.shutdown()
        else:
            print('Manual log prevention - Activated')
        return ipc_object

    def write_error_log(self, ipc_object=None, can_log=True):
        """write_error_log - Writes a error message into log file

        Keyword Arguments:
            ipc_object {InterProcessCommunicator}
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
                if ipc_object.data:
                    ipc_object.data['method_name'] = self.get_called_function_name()
                    ipc_object.message = "{ipc_object.module} | " + ipc_object.message
                    ipc_object.message = ipc_object.message.format(ipc_object=ipc_object)
                logger = logging.getLogger()
                logger.error(str(ipc_object.message))
            except Exception as ex:
                print(ex)
                ipc_object.success = False
                self.__write_log_exception()
            finally:
                logging.shutdown()
        else:
            print('Manual log prevention - Activated')
        return ipc_object

    def write_warning_log(self, ipc_object=None, can_log=True):
        """write_warning_log - Writes a warning message into log file

        Keyword Arguments:
            ipc_object {InterProcessCommunicator}
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
                if ipc_object.data:
                    ipc_object.data['method_name'] = self.get_called_function_name()
                    ipc_object.message = "{ipc_object.module} | " + ipc_object.message
                    ipc_object.message = ipc_object.message.format(ipc_object=ipc_object)
                logger = logging.getLogger()
                logger.warning(str(ipc_object.message))
            except:
                ipc_object.success = False
                self.__write_log_exception()

            finally:
                logging.shutdown()
        else:
            print('Manual log prevention - Activated')
        return ipc_object

    def write_critical_log(self, ipc_object=None, can_log=True):
        """write_critical_log - Writes a critical message into log file

        Keyword Arguments:
            ipc_object {InterProcessCommunicator}
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
                if ipc_object.data:
                    ipc_object.data['method_name'] = self.get_called_function_name()
                    ipc_object.message = "{ipc_object.module} | " + ipc_object.message
                    ipc_object.message = ipc_object.message.format(ipc_object=ipc_object)
                logger = logging.getLogger()
                logger.critical(str(ipc_object.message))
            except:
                ipc_object.success = False
                self.__write_log_exception()
            finally:
                logging.shutdown()
        else:
            print('Manual log prevention - Activated')
        return ipc_object

    def write_default_log(self, ipc_object=None, can_log=True):
        """write_default_log - Writes a message into log file, based on given
                                log level

        Keyword Arguments:
            ipc_object {InterProcessCommunicator}
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
                logger = __initiate_logger(ipc_object)
                error_level = ipc_object.level.lower()
                message = ipc_object.message

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
                ipc_object.success = False
                self.__write_log_exception()
            finally:
                logging.shutdown()
        else:
            print('Manual log prevention - Activated')
        return ipc_object

    def __write_log_exception(self):
        """__write_log_exception - Writes exception log for Logger occurs

        Returns:
            [InterProcessCommunicator]
                -- IPC Object which holds basic communication data
        """

        called_function_name = self.get_called_function_name()
        ipc_object = InterProcessCommunicator()
        ipc_object.module = 'LogProvider'
        ipc_object.message = 'Unable to load Logger/ Logger not available in '
        ipc_object.message = ipc_object.message + called_function_name
        self.write_critical_log(ipc_object)

        return ipc_object

    def get_called_funciton_name_with_module(self):
        innerframe = inspect.currentframe()
        outerframes = inspect.getouterframes(innerframe)

        for index, frame in enumerate(outerframes):
            if(frame.function == "get_called_funciton_name_with_module"):
                index += 2
                break

        called_function_name = (outerframes[index].function)
        if(called_function_name != "<module>"):
            called_function_name += "()"
        module_name = self.__get_bot_name__(outerframes[index].filename)
        called_function_name = str(module_name + '.' + called_function_name)

        return called_function_name

    def get_called_function_name(self):
        innerframe = inspect.currentframe()
        outerframes = inspect.getouterframes(innerframe)

        for index, frame in enumerate(outerframes):
            if(frame.function == "get_called_function_name"):
                index += 2
                break

        called_function_name = (outerframes[index].function)
        if(called_function_name != "<module>"):
            called_function_name += "()"

        return called_function_name

    def __get_parent_directory(self, file_name):
        expanded_dir = os.path.expanduser(file_name)
        realpath_dir = os.path.realpath(expanded_dir)
        directory = os.path.dirname(realpath_dir)
        return directory

    def __CONFIG_FILE_NAME(self):
        log_path = self.__get_parent_directory(__file__)
        if(os.path.exists(log_path)):
            return os.path.join(log_path, 'logger.ini')
        else:
            return os.path.join(os.getcwd(), 'logger.ini')

    def __get_bot_name__(self, file_name):
        return os.path.splitext(self.__get_file_name__(file_name))[0]

    def __get_file_name__(self, file_name):
        return os.path.basename(file_name)

    def config_logger_from_file(self, config_file):
        logging.config.fileConfig(config_file)
        return None
