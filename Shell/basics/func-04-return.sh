#!/bin/sh

# 함수
#`expr $1 + $2` 2개의 인자를 받아서 덧셈을 한 후 출력한다.
# 함수의 리턴값: $?
sum() {
	result=$(($1 + $2))
	echo "sum: $result"
	return $result
}

a=10
b=20
sum $a $b

# 함수의 리턴값: $?
echo "함수 sum($a + $b) -> ($?)"
exit 0
