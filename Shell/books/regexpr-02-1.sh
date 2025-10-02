#!/bin/bash

# q로 시작하고 임의의 소문자가 0개 이상이며 
# 마지막 문자가 '?'인 문자열을 찾음
# grep -E : 확장 정규 표현식
grep -E 'q[[:lower:]]*\?' ./expression.txt

# result:
# Do you have any questions? or Do you need any help?

