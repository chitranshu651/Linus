#!/bin/bash
#
# A simple timer using bash.
# In commad line pass time in sec as first argument
#	TO display a specific messege add that as second command line argument.
#

var=$1
while [ $var -gt 0 ];
do
	var=$(($var-1))
	sleep 1
done

if [ $# == 2 ]; then
	echo $2
	notify-send $2
else
	echo "Times Up"
	notify-send "Times up"
fi
