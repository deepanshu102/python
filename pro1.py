import os
import time
curDir=os.getcwd(); ## Current running Directory
print(curDir);
os.mkdir('NEW DIR');#create a directory
time.sleep(2);#sleep for 2sec but we can put time on miliseconds
os.rename('NEW DIR','NewDir');## rename the existence directory(NEW DIR)
time.sleep(2);
os.rmdir('NewDir');##Remove the Directory
print(os.getenv('path')) ## show the Enviroment Path
import datetime
now=datetime.datetime.now(); ## store current date and time
print(now);
print(now.year); ## print specific year
