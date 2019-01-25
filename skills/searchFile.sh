#!/bin/bash

if [ $# == 0 ]; then
	echo "Enter filename"
elif [ $# == 1 ]; then
	var=`ls | grep -x $1`
	if [ "x$var" != "x" ]; then
		var=`ls -l | grep $1`
		echo $var
	else
		echo "File not found"
		#exit(1)
	fi
else
	cd $2
	var=`ls | grep -x $1`
	if [ "x$var" != "x" ]; then
		var=`ls -l | grep $1`
		echo $var
	else
		echo "File not found"
		#exit(1)
	fi
fi
