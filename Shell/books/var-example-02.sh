#!/bin/bash

function parsing() {
	STR=$1
	LEN=${#STR}
	echo "원본문자열: ${STR}"
	echo "문자열길이: ${LEN}"

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
}

