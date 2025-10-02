#!/bin/bash

# 라인의 시작과 종료 문자가 대괄호로 시작하고 끝나며
# 대괄호 안에는 알파벳과 숫자로 구성
grep -i -e "^\[[[:alnum:]]*\]" ./expression2.txt

