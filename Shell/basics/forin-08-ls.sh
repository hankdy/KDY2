#!/bin/sh

# 파일 목록 출력하기

echo "[확장자가 '*.sh'인 파일 목록 보기]"

for filename in $(ls *.sh)
do
	echo $filename
done

exit 0
