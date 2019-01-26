#!/bin/bash

c="ls /usr/lib/jvm | grep java"
ere=$(eval $c)

var=$(echo $ere | rev | cut -d " " -f1 | rev)
echo $var
konsole -e  "sudo archlinux-java set $var"
