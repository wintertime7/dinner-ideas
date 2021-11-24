#!/bin/bash
#define the storage to take missing files from
local_storage="/dinner_ideas_storage"

echo "Script to setup environment"

#this code tests if the configuration file exists, if not, then it copies it from the storage directory
echo "------------------------------"
echo "Checking if config.ini file exists in current directory..."
if test -f "config.ini"; then
	echo "exists"
else
	echo "Copying config file from local storage..."
	cp $HOME$local_storage/config.ini .
	if [ $? -eq 0 ]; then echo "OK"; else echo "Problem copying config.ini file"; exit 1; fi
fi

#this code tests if logs directory exists, if not, then it makes the directory
echo "------------------------------"
echo "Checking if logs directory exists in current directory..."
if test -d "logs"; then
	echo "exists"
else
	echo "Creating logs directory..."
	mkdir logs
	if [ $? -eq 0 ]; then echo "OK"; else echo "Problem creating logs directory"; exit 1; fi
fi

#this code tests if the logs file exists in the logs directory, if not, then it creates one
echo "------------------------------"
echo "Checking if logs file exists in current directory..."
if test -f "logs/dinner_ideas_log.log"; then
	echo "exists"
else
	echo "Creating the logs file..."
	touch logs/dinner_ideas_log.log
	if [ $? -eq 0 ]; then echo "OK"; else echo "Problem creating logs file"; exit 1; fi
fi

#this code tests if migrations directory exists, if not, then it makes the directory
echo "------------------------------"
echo "Checking if migrations directory exists in current directory..."
if test -d "migrations"; then
	echo "exists"
else
	echo "Creating migrations directory..."
	mkdir migrations
	if [ $? -eq 0 ]; then echo "OK"; else echo "Problem creating migrations directory"; exit 1; fi
fi

#this code finds the python 3 executable location for further tests
echo "------------------------------"
echo "Getting Python3 executable location..."
python_exec_loc=$(which python3)
if [ $? -eq 0 ]; then echo "OK"; else echo "Problem getting Python3 exec location"; exit 1; fi
echo "$python_exec_loc"

#this code runs the automatic test python file
echo "------------------------------"
echo "Running automatic test..."
$python_exec_loc dinner_ideas_auto_test.py
if [ $? -eq 0 ]; then echo "OK"; else echo "Automatic test FAILED"; exit 1; fi
echo "------------------------------"

echo "All tests have been successful, the code can be executed... good luck & have fun!"