#!/bin/bash

# q로 시작하고 임의의 소문자가 0개 이상이며 
# 마지막 문자가 '?'이거나 임의의 문자 하나와 일치하는 문자열
# grep -E : 확장 정규 표현식
grep -E 'q[[:lower:]]*\??' ./expression.txt

# result: 'questions' 다음에 ?나 ,가 나오는 문자열을 찾음
# Do you have any questions? or Do you need any help?
# If you have any questions, Please send a mail to the email below.


