#!/bin/sh

fname='./test.txt'

# [문제]
# 파일이 존재하는 검사 후 : -e
# 읽을수 있는 파일(-f)이면서 크기가 0이 아닌 경우(-s)
# OR : ||, -o
if [ -e $fname ]
then
	if [ \( -r $fname \) -o \( -w $fname \) ]
	then
		cat $fname
	else
		echo "$fname은 파일 읽기 불가이거나 크기가 0입니다."
	fi
else
	echo "$fname 파일이 존재하지 않습니다."
fi

exit 0
