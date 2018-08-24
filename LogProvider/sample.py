try:
    # Import Logger from outside the Module
    from LogProvider import Logger as logger
except:
    # Import Logger from inside the Module
    import Logger as logger

import os

# Creates IPC object with basic ipc structure
ipc_object = logger.InterProcessCommunicator()

bot_name, extention =   os.path.splitext(os.path.basename(__file__))

# Populating IPC object
ipc_object.module = bot_name
ipc_object.message = 'Test Message'

logger.write_info_log(log_object=ipc_object)
logger.write_error_log(log_object=ipc_object)
logger.write_debug_log(log_object=ipc_object)
logger.write_warning_log(log_object=ipc_object)
logger.write_critical_log(log_object=ipc_object)

