#!/bin/sh

# 조건문
# 같은가? : =
if [ "hello" = "hello" ]
then
	echo "참이다"
fi

if [ 'hello' = "hello" ]
then
	echo "참이다"
fi

if [ 'hello' = "Hello" ]
then
	echo "참이다"
fi

exit 0

