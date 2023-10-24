#!/usr/bin/env bash
# Package file getter


if (( $# == 0 ))
then
	echo "Usage: git_file <url to github file>"
	exit 1
fi

echo -e "\n" > .gets.log
echo -e "Entered URL" >> .gets.log
echo "++++++++++++++++++++++++++++++++++++++++++++++++++" >> .gets.log
echo "$1" >> .gets.log
echo "++++++++++++++++++++++++++++++++++++++++++++++++++" >> .gets.log
echo "================================================" >> .gets.log
echo "$1" | ~/git_copy/py_get >> .gets.log 2>&1
value=$?

if (( $value == 0 ))
then
	echo -e "\033[0;32m-----------OK-------------\033[0m"
	echo "================================================" >> .gets.log
	echo -e "\n" >> .gets.log
	exit 0
else
	echo -e "\033[0;31m---------------------FAILED-----------------------\033[0m"
	# print error message to screen
	echo "Sorry an error occured"
	echo -e "+++++++"
	echo -e "-------"
	cat .gets.log | tail -5
	echo "for more error details open .gets.log"
	echo -e "\033[0;31m--------------------------------------------------\033[0m"
	exit 1
fi
