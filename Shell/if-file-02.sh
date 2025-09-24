#!/bin/sh

fname='./test.txt'

if [ -s $fname ]
then
	cat $fname
else
	echo "파일($fname)의 크기가 0입니다."
fi

exit 0
