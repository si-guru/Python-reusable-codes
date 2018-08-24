# ------------------------------------------------------------------ #
# Author		- AVM-Automation (Cognizant)                         #
# Module name	- DataObject                                         #
# Version		- 1.0												 #		 												#
# Description	- This is custom python module contains data object  #
#                which can be used in various operations including   #
#                inter-process communication                         #
# ------------------------------------------------------------------ #

class JSONList(object):
  """JSONList - A custom class, which convert python list/ tuple object into a collection of __dict__ object and
      store it in 'list' variable
  """
  def __init__(self, list_value = None):
    sample = []
    for data in list_value:
      sample.append(data.__dict__)
    self.list		= sample
    return  None

class ProcessData(object):
  """ProcessData - A customised class which holds details for inter-process communication
  """
  def __init__(self, data = None, message = None, status = None, level = None, name = None):
    self.data     = data
    self.message  = message
    self.status   = status
    self.level    = level
    self.name     = name
    return None

def object_to_json(object = None):
  """object_to_json -  This function converts an object into __dict__ object which in turn can be used as JSON

  Arguments:
    object {object} -- Any valid python object

  Returns:
    __dict__ -- The dictionary value of python object or None if the object is not valid
  """
  if(not object):
    return None
  if(isinstance(object, list) or isinstance(object, tuple)):
    object		= JSONList(object)
  return object.__dict__

