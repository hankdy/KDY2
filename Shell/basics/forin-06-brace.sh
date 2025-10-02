#!/bin/bash

# bash SHELL
# 중괄호(brace) : { ... }
# {시작..종료}
# {시작..종료..증가}

# 1부터 10까지의 홀수의 합

hap=0

# 1부터 10까지 2씩 증가
for i in {1..10..2}
do
	hap=`expr $hap + $i`
	echo "i=$i -> $hap"
done

echo "1부터 10까지의 홀수의 합은 $hap"
exit 0
