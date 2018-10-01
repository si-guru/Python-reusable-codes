"""
Name            :   Logger
Usage           :   Allows Logging functionality using python
Reusability     :   Completely Reusable
Author          :   AVM-Automation-SGO
Created on      :   06/06/2018
Compatibility   :   Python 3.5+
------------------------------------------------------------------------------
Change Log: Recent Modification in TOP
------------------------------------------------------------------------------
Date        Moderator   Ver     Comments
------------------------------------------------------------------------------
09/10/2018  DomainBOTS  1.13    Added get_called_function_name
                                Added get_called_funciton_name_with_module
                                Modified InterProcessCommunicator
                                Modified Log_Constants as seperate module
                                Modified InterProcessCommunicator as seperate module
                                Modified ContextFilter as seperate module
                                Moved Logger functions to log_functions module
                                Added log_functions.logger method references
09/05/2018  DomainBOTS  1.12    Added __get_file_name__
                                Added Log_Constants Class
                                Modified log method's param name from
                                log_object to ipc_object
                                Modified all log methods to use
                                {InterProcessCommunicator.data}
08/13/2018  DomainBOTS  1.11    Modified Code as per PEP8 and pyLint standards
06/06/2018  DomainBOTS  1.10    Added a new function "write_default_log"
06/05/2018  DomainBOTS  1.01    Added docstrings to all functions
03/29/2018  AVM         1.00    Initial Code
"""



# Custom modules
from . import log_constants as Log_Constants
from .IPC import InterProcessCommunicator
from .log_filters import ContextFilter
from .log_functions import logger

logger = logger()
# Used for backward compatibility/ Interface
get_called_funciton_name_with_module = logger.get_called_funciton_name_with_module
get_called_function_name = logger.get_called_function_name
write_critical_log = logger.write_critical_log
write_debug_log = logger.write_debug_log
write_default_log = logger.write_default_log
write_error_log = logger.write_error_log
write_info_log = logger.write_info_log
__get_bot_name__ = logger.__get_bot_name__
__get_file_name__ = logger.__get_file_name__

# Self Logging
module = 'Logger'
log_constants = Log_Constants
ipc_object = InterProcessCommunicator(module=module)
bot_name = ipc_object.module
ipc_object.data = {}
ipc_object.data['package_name'] = bot_name
ipc_object.message = log_constants.INFO_PACKAGE_LOAD
logger.write_info_log(ipc_object)
