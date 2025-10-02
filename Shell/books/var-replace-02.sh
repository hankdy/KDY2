#!/bin/bash

# 변수의 문자열 값을 변경하기 위한 매개변수 확장자
FILE_NAME="myvm-container-repo.tar.gz"

# ${변수##패턴}
# 변수에 설정된 문자열 앞에서부터 마지막으로 찾은 패턴과 일치하는
# 패턴 앞의 모든 문자열을 제거
echo ${FILE_NAME##*-}

# 결과: repo.tar.gz
