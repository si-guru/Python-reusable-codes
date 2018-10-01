"""
Name            :   IPC
Usage           :   The IPC has classes and function which can be used for
                    inter process communication
Reusability     :   Completely Reusable
Author          :   DomainBOTS
Created on      :   09/10/2018
Compatibility   :   Python 3.5+
-----------------------------------------------------------------------------
Change Log: Recent Modification in TOP
------------------------------------------------------------------------------
Date        Moderator   Ver     Comments
------------------------------------------------------------------------------
09/10/2018  DomainBOTS  1.00    Initial Code
"""


class InterProcessCommunicator(object):
    """InterProcessCommunicator - A customised class which holds basic details
        for inter-process communication
    """
    data = None
    message = None
    status = None
    level = None
    success = None
    module = None

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
        message = str(message + "InterProcessCommunicator" +
                    " - Used for communcation between process\n")
        message += str("Module : " + str(self.module) + "\n")
        message += str("Level : " + str(self.level) + "\n")
        return message