#!/bin/bash
#
# Enter path to music folder as commad line argument
# A file .music will be created at home folder of user
#
#

rm -f ~/.music.txt
if [ $# == 0 ]; then
	echo "Enter Path"
fi

`find $1 -name "*.mp3" -o -name "*.ogg" -o -name "*.wav" >> ~/.music.txt`

var=""
while IFS= read line
do
		line=$(echo $line | sed 's/ /\\ /g')
		#echo 1 $line
    var="$var "$line""
done <".music.txt"
echo $var
nvlc --started-from-file --playlist-enqueue $var
rm -f ~/.music.txt
