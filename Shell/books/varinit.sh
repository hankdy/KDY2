#!/bin/bash

# 변수 초기화(할당, 치환)하기 위한 확장 변경자

# 변수가 설정되지 않은 경우 문자열로 변수를 치환
echo ${OSX-ubuntu}  # ubuntu

# 변수가 설정되지 않았거나 NULL로 설정된 경우 문자열로 변수를 치환
echo ${OSX:-ubuntu} # ubuntu

#
OS1=""
# 변수가 설정되지 않은 경우 문자열을 변수에 저장하고 변수 치환
echo ${OS1=ubuntu}  # 

# 변수가 설정되지 않았거나 NULL인 경우 문자열을 변수에 저장하고 변수 치환
echo ${OS1:=ubuntu} # ubuntu

