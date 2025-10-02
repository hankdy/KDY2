#!/bin/sh

# 함수
# 2개의 인자를 받아서 덧셈을 한 후 출력한다.
sum() {
	result=$(($1 + $2))
	echo "$result"
}

a=10
b=20
sumresult=$(sum $a $b)

# 함수의 리턴값: $?
echo "함수 sum($a + $b) -> ($sumresult)"
exit 0
