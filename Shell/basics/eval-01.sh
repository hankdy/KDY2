#!/bin/sh

# eval은 문자열에 담긴 명령어 실행
# 문자열에는 실행 가능한 명령어가 들어 있어야 한다.

str="ls -l eval*"

echo $str
eval $str
exit 0
