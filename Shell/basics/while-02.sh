#!/bin/sh

# 무한루프: 1은 참
# 조건이 만족하면 계속 반복 실행
# 정지: Ctrl+S
# 실행: Ctrl+Q
# 종료: Ctrl+C

cnt=0

while [ 1 ]
do
	cnt=$((cnt+1))
	echo "우분투  24.04.3 LTS:" $cnt
done

exit 0
