#!/bin/sh

echo "문자열을 입력하세요:"
read hello
echo "입력받은 문자열:" $hello

# -n "문자열" : 문자열이 NULL(빈문자열)이 아니면 참
if [ -n "$hello" ]
then
	echo "'$hello'는 NULL이 아닙니다."
else
	echo "'$hello'는 NULL입니다."
fi

exit 0
