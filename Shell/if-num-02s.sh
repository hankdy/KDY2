#!/bin/sh

# 문자열
num1='100'
num2=200

# expr로 처리를 하면 숫자로 변환해서 연산을 수행
num3=`expr $num1 + $num2`  # 300
echo 'num3: ' $num3

# -ne : Not Equal, 숫자비교
if [ $num1 -ne $num2 ]
then
	echo "$num1과 $num2은 다르다."
else
	echo "$num1과 $num2은 같다."
fi
exit 0

