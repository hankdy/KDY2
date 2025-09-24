#!/bin/sh

echo '변수(hello) :' "$hello"

hello=''

# -z "문자열" : 문자열이 NULL(빈문자열)이면 참
if [ -z $hello ]
then
	echo "'$hello'는 NULL입니다."
else
	echo "'$hello'는 NULL이 아닙니다."
fi

# -z "문자열" : 문자열이 NULL(빈문자열)이면 참
if [ -z "$hello" ]
then
	echo "'$hello'는 NULL입니다."
else
	echo "'$hello'는 NULL이 아닙니다."
fi
exit 0
