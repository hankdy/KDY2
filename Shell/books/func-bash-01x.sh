#!/bin/bash

# bash에서 함수 정의 부분에 function 키워드를 붙인다.
# 실행: bash func-bash-01.sh
# 함수 정의를 일반 SHELL 형태로 정의하면?
# sh, bash 모두 정상적으로 실행된다.
print() {
	echo $1
}

print "I can speak Korean"
