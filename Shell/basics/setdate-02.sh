#!/bin/sh

# set $(명령어)를 하게되면 출력 결과가 파라미터에 세팅된다.
# $1, $2, ...에 저장된다.

echo "오늘 날짜는 $(date)입니다"
set $(date)
 
echo "전체 파라미터: $*"

for p in $*
do
	echo "파라미터: $p"
done
exit 0
