#!/bin/bash

# 예제5) 메타문자 {N,M}, $ 그리고 문자클래스 [:alpha:], [:digit:]를 이용할 경우

# 라인 종료 시 알파벳 4글자 이상 6글자 이하인 단어가 있는 라인
grep -E '[[:alpha:]]{4,6}$' ./expression.txt

# result:
# Regular Expression
# Author: NaleeJang
# Description: regular expression test file
# System Information
# Help
# Contacts

