#!/bin/bash

# 변수의 문자열 값을 변경하기 위한 매개변수 확장자
FILE_NAME="myvm-container-repo.tar.gz"

# 변수의 길이
echo "변수의 길이: ${#FILE_NAME}"

# ${변수%패턴}
# 변수에 설정된 문자열 뒤에서부터 처음 찾은 패턴과 일치하는 패턴 뒤의 모든 문자열 제거
echo ${FILE_NAME%.*}
# 결과: myvm-container-repo.tar

# ${변수%%패턴}
# 변수에 설정된 문자열 뒤에서부터 마지막으로 찾은 패턴과 일치하는 패턴 뒤의 모든 문자열 제거
echo ${FILE_NAME%%.*}

# 결과: myvm-container-repo
