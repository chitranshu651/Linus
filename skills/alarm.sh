#!/bin/bash
#
# Pass hr and min in command line arg.
# always add 0 before single digit number. Ex: 7 -> 07
# Add Message to display in command line too


hr=`date "+%T" | cut -d ":" -f1`
min=`date "+%T" | cut -d ":" -f2`

while [ $1 != $hr ]
do
	hr=`date "+%T" | cut -d ":" -f1`
done

while [ $2 != $min ]
do
		min=`date "+%T" | cut -d ":" -f2`
done

if [ $# == 3 ]; then
	echo $3
	notify-send $3
else
	echo "Times Up"
	notify-send "Times up"
fi
