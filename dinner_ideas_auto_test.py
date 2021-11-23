from genericpath import exists
import os

from configparser import ConfigParser

#checking if config file exists
print('-----------------')
print('Checking if config file exists...')
assert os.path.exists('config.ini') == True
print('OK')

#opening the config file
config = ConfigParser()
config.read('config.ini')

#checking if the config file has login credentials for developer 1
print('-----------------')
print('Checking if config file has login credentials...')
assert config.has_option('developers', 'dev1_uname') == True
assert config.has_option('developers', 'dev1_pass') == True
print('OK')

#checking if the logs directory exists
print('-----------------')
print('Checking if log directory exists...')
assert os.path.isdir('logs') == True
print('OK')

#checking if log file exists
print('-----------------')
print('Checking if log file exists...')
assert os.path.isfile('logs/dinner_ideas_log.log')
print('OK')

#checking if migrations directory exists
print('-----------------')
print('Checking if migrations directory exists...')
assert os.path.isdir('migrations')
print('OK')
print('-----------------')

print('Automatic basic setup test done!')
print('-----------------')
