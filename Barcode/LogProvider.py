
""" 
Author      	- AVM-Automation (Cognizant)                       
Module name		- LogProvider                                      
Version     	- 1.0											   
Description		- This is custom python module contains data object
               	which can be used in various operations including 
               	inter-process communication           

"""
try:
	from	.CustomLogger	import	Logger
	from	.DataObject		import	ProcessData
except:
	from	CustomLogger	import	Logger
	from	DataObject		import	ProcessData
import	inspect

def insert_log(log_data	=	None):
	"""insert_log - A common function which logs data as it is

	Returns:
		log_data[DataObject.ProcessData] -- returns the log_data data as it is.
	"""

	try:
		
		Logger.log_message(str(log_data.name), str(log_data.message), str(log_data.level))
	except Exception as exception:
		print('Log Exception - @ insert_log - ',exception)
	return log_data

def insert_error_log(log_data	=	None):
	"""insert_error_log - A common function which logs error data

	Returns:
		log_data[DataObject.ProcessData] -- returns the log_data data as it is.
	"""
	try:
		Logger.log_message(log_data.name, log_data.message, ERROR())
	except Exception as exception:
		print('Log Exception - @ insert_error_log -',exception)
	return log_data

def insert_warn_log(log_data	=	None):
	"""insert_warn_log - A common function which logs warn data

	Returns:
		log_data[DataObject.ProcessData] -- returns the log_data data as it is.
	"""
	try:
		Logger.log_message(log_data.name, log_data.message, WARN())
	except Exception as exception:
		print('Log Exception - @ insert_warn_log - ',exception)
	return log_data

def insert_info_log(log_data	=	None):
	"""insert_info_log - A common function which logs info data

	Returns:
		log_data[DataObject.ProcessData] -- returns the log_data data as it is.
	"""
	try:
		Logger.log_message(log_data.name, log_data.message, INFO())
	except Exception as exception:
		print('Log Exception - @ insert_info_log - ',exception)
	return log_data

def insert_debug_log(log_data	=	None):
	"""insert_debug_log - A common function which logs debug data

	Returns:
		log_data[DataObject.ProcessData] -- returns the log_data data as it is.
	"""
	try:
		Logger.log_message(log_data.name, log_data.message, DEBUG())
	except Exception as exception:
		print('Log Exception - @ insert_debug_log - ',exception)
	return log_data

def insert_critical_log(log_data	=	None):
	"""insert_critical_log - A common function which logs critical data

	Returns:
		log_data[DataObject.ProcessData] -- returns the log_data data as it is.
	"""
	try:
		Logger.log_message(log_data.name, log_data.message, CRITICAL())
	except Exception as exception:
		print('Log Exception - @ insert_critical_log - ',exception)
	return log_data

def insert_no_log():
	innerframe	= inspect.currentframe()
	outerframes	=	inspect.getouterframes(innerframe)
	called_function	= str(outerframes[1][3])
	Logger.log_message('LogProvider',	'Unable to load Logger/ Logger not available in '	+	called_function,	CRITICAL())
	return ProcessData()

def generate_process_data(bot_name	=	None):
	try:
		process_data					=	ProcessData()
		process_data.name			=	bot_name
		process_data.level		=	INFO()
		process_data.message	=	'Bot Loaded'
		insert_log(process_data)
		return process_data
	except:
		insert_no_log()

# Functions which returns a constant value - Workaround for constants in python
def INFO():
	return 'info'

def ERROR():
	return 'error'

def DEBUG():
	return 'debug'

def WARN():
	return 'warn'

def CRITICAL():
	return 'critical'
