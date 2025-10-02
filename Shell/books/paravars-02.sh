#!/bin/bash

echo "매개변수의 총 갯수: <$#>"
echo "전체 파라미터: <$@>"

for language in $@
do
	echo "I can speak '$language'"
done

exit 0

# 파라미터: Korean, English, "Japaness Chinese"
# 결과: 
#  - 공백 기준으로 문자열을 분리해서 인식
#  - 총 4개의 파라미터로 처리
#    Korean
#    English
#    Japaness
#    Chinese
