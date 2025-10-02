#!/bin/bash

# 예제5) 메타문자 {N,M}, $ 그리고 문자클래스 [:alpha:], [:digit:]를 이용할 경우

# 라인 종료 시 숫자 4글자 이상 6글자 이하인 단어가 있는 라인
# 라인의 맨 마지막 문자는 임의의 문자(특수문자, 숫자, 영문자)
grep -E '[[:digit:]]{4,6}.$' ./expression.txt

# 같은 결과
grep -E '[[:digit:]]{4,}.$' ./expression.txt

# result:
# Today is 05-May-2020.


