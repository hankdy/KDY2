#!/bin/sh

# until문은 조건식이 참일 때까지 반복
# 즉 거짓인 동안 반복하며 참이되면 루프를 탈출
hap=0
cnt=1

# cnt가 10보다 크면 즉 11이 되면 루프를 탈출
# -gt : great than
until [ $cnt -gt 10 ]
do
	hap=`expr $hap + $cnt`
	cnt=`expr $cnt + 1`
done

echo "1부터 10까지의 합: $hap"
exit 0

