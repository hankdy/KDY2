#!/bin/bash

# 예제3) 메타 문자 +와 ^를 이용할 경우

# '-2'로 시작해서 '-'로 끝나며, 2가 계속 반복
grep -E '\-2+\-' ./expression.txt

# result:
# phone: 010-2222-5668

# 라인의 시작 문자가 '#'으로 시작되는 라인
grep '^#' ./expression.txt

# result:
#===========================================#
# Date: 2020-05-05
# Author: NaleeJang
# Description: regular expression test file
#===========================================#
# System Information
# Help
# Contacts

