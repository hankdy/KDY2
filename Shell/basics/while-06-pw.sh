#!/bin/sh

# [문제]
# 비밀번호를 입력하지 않고 그냥 Enter를 쳤을 때 오류가 나오지 않도록 아래의 코드를 수정하라.

mypass='0000'

# 조건식이 참이면 반복
# 패스워드가 다르면 반복하여 같아지만 탈출
while [ $mypass != "1234" ]
do
	echo -n "비밀번호를 입력하세요: "
	read mypass
	# 변수가 NULL(빈문자열)이면 참
	if [ -z "$mypass" ] # Enter, Space + Enter
	then
		echo "[오류] 비밀번호를 입력하지 않았습니다."
		mypass="0000"
	else
		if [ $mypass != "1234" ]
		then
			echo "[오류] 비밀번호가 틀렸습니다."
		fi
	fi
done

echo "통과!!!"
exit 0

