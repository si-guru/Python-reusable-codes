Tool: Logger
Author : AVM-Automation(Cognizant)
Date : 12/19/2017
Version : V1
Environment: Python 2.7.12
Output: (.Log) File

Objective:
---------
	This python script will log the message based upon the setting in the configuration file.

Reason for Developement:
------------------------
	Tracking/Reading the log for each bot separately is tedious task. This python script will capture the Debug/info/error/critical error/warning Message in the single/multiple repository based on the user defined.

User:
-----
	1) Developer/Automation Engineer

File Dependency:
----------------
	1) Logger.ini(Currently modify the path in script placed in dir. This  
dependency will removed in upcoming version).
Note: User can modify the type of logging in configuration file. Currently  
TimeRotatingHandler is used which will refresh on every Monday and backup older version 
up to 5 level. For more info.
      https://docs.python.org/2/library/logging.handlers.html


File-Info:
----------
   Logger has three level.
	1) Loggers - Don't modify root level.
	2) Handlers - This will define where the message need to store. We can even track error message alone separate file in addition to normal logging. Please refer link above.
	3) Formatter - How message need to be displayed. For single handler , one formatter is required.
   Please read logging for python.


How to run Logger:
------------------
1) keep the logger script/ini file shared in the common directory
2) Update the logger path in the script "logPath" to the current directory(one time activity)
3) Then in the bot, define syspath to refer the logger script.
4) Import Logger.
5) To log Message, call Logger.log_message(botname,message,errorlevel)
Accepted error level are debug,info,warn,error,critical
6) To get the botname, please use the "os.path.splitext(os.path.basename(__file__))[0]" function.


Sample Log:
-----------
1) Modify loggerPath and run the script.
import sys, os
loggerPath=r'C:\Users\445781\Documents\Python\Temporary-Version'
sys.path.append(loggerPath)
import Logger
botName=os.path.splitext(os.path.basename(__file__))[0]
Logger.log_message(botName,'Started to execute','info')
try:
    import test1234
except Exception,e:
    Logger.log_message(botName,str(e),'error')
Logger.log_message(botName,'Finished  execution','warn')
print('Completed')








		
