#!/bin/bash

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
