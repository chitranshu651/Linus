#!/bin/bash

#Takes in 1 arguement version number 2 or 3
if [ $# == 0 ]; then
    echo "Not enough arguements"
elif [ $# == 1 ] ; then
    ty="python$1"
    echo $ty
    alias python=$ty
else
    echo "Too many arguements"
fi
    
