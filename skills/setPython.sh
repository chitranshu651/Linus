#!/bin/bash

if [ $# == 0 ]; then
    echo "Not enough arguements"
elif [ $# == 1 ] ; then
    ty="python$1"
    echo $ty
    alias python=$ty
else
    echo "Too many arguements"
fi
    
