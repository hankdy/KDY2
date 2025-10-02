#!/bin/bash

# 예제5) 메타문자 {N,M}, $ 그리고 문자클래스 [:alpha:], [:digit:]를 이용할 경우

# [문제]
# 아래에 예시된 전화번호를 추출하라
# 예: 010-1234-5678, 032-123-4567, 032-1234-5678

# grep -E '[[:digit:]]{2,3}\-[[:digit:]]{3,4}\-[[:digit:]]{4}' ./expression.txt
# grep -E '[[:digit:]]{2,3}-[[:digit:]]{3,4}-[[:digit:]]{4}' ./expression.txt
# grep -E '[[:digit:]]{2,3}-[[:digit:]]{3,4}-[[:digit:]]{4}' ./expression.txt
# egrep '[[:digit:]]{2,3}-[[:digit:]]{3,4}-[[:digit:]]{4}' ./expression.txt
egrep '[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}' ./expression.txt



