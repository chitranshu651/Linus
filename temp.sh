#!/bin/bash

echo $# $*
if [ $# == 0 ]; then
	echo 0
elif [ $# == 1 ];then
	echo 1
else
	echo 2+
fi
