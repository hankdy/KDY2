#!/bin/sh

# 외부 명령어
# seq : /usr/bin/seq

# 사용법: seq(시작 [간격] 종료)

# 훌수의 합
hap=0

# 1부터 2씩 증가하여 10까지
for i in $(seq 1 2 10)
do
	hap=`expr $hap + $i`
	echo "i=$i -> $hap"
done

echo "1부터 10까지의 홀수의 합은 $hap"
exit 0
