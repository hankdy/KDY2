#!/bin/sh

echo "비밀번호를 입력하세요:"
read mypass

# 조건식이 참이면 반복
# 패스워드가 다르면 반복하여 같아지만 탈출
while [ $mypass != "1234" ]
do
	echo "비밀번호가 틀렸습니다. 다시 입력하세요."
	read mypass
done

echo "통과!!!"
exit 0

