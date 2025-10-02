#!/bin/sh

# 문자열
num1='100'
num2=100

echo "num1: $num1"
echo "num2: $num2"

# -ge : Great Equal
if [ $num1 -ge $num2 ]
then
	echo "$num1은 $num2보다 크거나 같다."
else
	echo "$num1은 $num2보다 크거나 같지 않다."
fi
exit 0

