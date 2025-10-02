#!/bin/bash

STR=$1

echo "전체문자열: $*"
echo "원본문자열: ($1)"

LEN=${#STR}
echo "문자열길이: ${LEN}"

echo "[결과]"
while (($LEN > 0))
do
	echo ${STR%%.*}
	STR=${STR#*.}
	if [ $LEN -eq ${#STR} ]
	then
		break
	fi
	LEN=${#STR}
done


