#!/bin/sh

var1="지역변수"
export var2="외부변수"

echo $var1
echo $var2

# 다른 셸 스크립트를 실행
# exp1.sh에서 var2를 사용 가능
sh exp1.sh
exit 0
