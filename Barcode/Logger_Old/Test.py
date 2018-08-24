import sys, os
loggerPath=r'C:\Users\445781\Documents\Python\Temporary-Version'
sys.path.append(loggerPath)
import Logger
botName=os.path.splitext(os.path.basename(__file__))[0]
Logger.logMessage(botName,'Started to execute','info')
try:
    import test1234
except Exception,e:
    Logger.logMessage(botName,str(e),'error')
Logger.logMessage(botName,'Finished  execution','warn')
print('Completed')







