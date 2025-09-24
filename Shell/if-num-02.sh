#!/bin/sh

num1=100
num2=200

# -ne : Not Equal
if [ $num1 -ne $num2 ]
then
	echo "$num1과 $num2은 다르다."
else
	echo "$num1과 $num2은 같다."
fi
exit 0
