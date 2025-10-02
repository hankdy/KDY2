#!/bin/bash

echo "매개변수의 총 갯수: <$#>"
echo "전체 파라미터: <$*>"

# 따옴표로 감싸면("$*") 파라미터 전체를 
# 하나의 문자열로 처리한다.
for language in "$*"
do
	echo "I can speak '$language'"
done

exit 0

# 파라미터: Korean, English, "Japaness Chinese"
# 결과: Korean English Japaness Chinese

