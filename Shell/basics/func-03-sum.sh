#!/bin/sh

# 함수
# 2개의 인자를 받아서 덧셈을 한 후 출력한다.
sum() {
	echo `expr $1 + $2`
}

a=10
b=20
sum $a $b
exit 0
