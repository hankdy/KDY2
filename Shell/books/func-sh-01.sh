#!/bin/sh

# 실행(bash func-sh-01.sh)하면 정상적으로 실행된다.
# 그러나 실행모드(chmod +x)를 바꾼 후 
# 실행(func-sh-01.sh)하면 오류가 나온다.
# 이유는 function 키워드는 bash에서만 허용한다.
function print() {
	echo $1
}

print "I can speak Korean"
