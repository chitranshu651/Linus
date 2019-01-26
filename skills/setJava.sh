#!/bin/bash
#Pass two arguements 1st is version and 2nd is blank or open
n="java-$1-$2jdk"
konsole -e  "sudo archlinux-java set $n"
