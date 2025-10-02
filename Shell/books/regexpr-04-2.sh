#!/bin/bash

# 예제4) 메타문자 ^, {N}, {N,} 그리고 문자클래스 [:alpha:]를 이용한 경우 

# 라인의 시작 시 알파벳 5글자 이상이며, 뒤에 공백을 가진 단어가 있는 라인
grep -E '^[[:alpha:]]{5,}[[:space:]]' ./expression.txt

# result:
# Today is 05-May-2020.
# Current time is 6:04PM.
# Memory size is 32GiB

# 맨 마지막 문자가 SPACE인 경우
echo "---------------------------------------------"
echo "맨 마지막 문자가 SPACE인 경우"
grep -E '^[[:alpha:]]{5,}[ ]' ./expression.txt
echo "---------------------------------------------"
grep -E '^[[:alpha:]]{5,}\ ' ./expression.txt

exit 0
