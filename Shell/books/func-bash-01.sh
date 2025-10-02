#!/bin/bash

# bash에서 함수 정의 부분에 function 키워드를 붙인다.
# 실행: bash func-bash-01.sh
function print() {
	echo $1
}

print "I can speak Korean"
