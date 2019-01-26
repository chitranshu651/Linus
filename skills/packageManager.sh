#!/bin/bash
#
# Enter package name in commad line argument
#
#	script will search for that package in pacman
#	if not found then it will search in AUR with help of yay
#
#

sudo pacman -S $1

if [ $? == 1 ]; then
		yay $1
fi
