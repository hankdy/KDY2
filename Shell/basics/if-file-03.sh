#!/bin/sh

fname='./test.txt'

# 읽을수 있는 파일이면서 크기가 0이 아닌 경우
# AND : &&
if [ -f $fname ] && [ -s $fname ]
then
	cat $fname
else
	echo "$fname은 파일이 아니거나 크기가 0입니다."
fi

exit 0
