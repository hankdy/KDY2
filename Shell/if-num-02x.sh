#!/bin/sh

# 문자열
num1='hello'
num2='world'

# -ne : Not Equal
if [ $num1 -ne $num2 ]
then
	echo "$num1과 $num2은 다르다."
else
	echo "$num1과 $num2은 같다."
fi
exit 0

# 처리결과: 아래와 같이 오류가 발생되지만 if의 else가 처리된다.
# Illegal number: hello
# 'hello과 world는 같다'가 출력된다.
