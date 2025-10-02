#!/bin/sh

hap=0
cnt=1

while [ $cnt -le 10 ]
do
	hap=$((hap + cnt))
	cnt=$((cnt + 1))
done

echo "1부터 10까지의 합: $hap"
exit 0

