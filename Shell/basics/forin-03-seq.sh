#!/bin/sh

hap=0

for i in $(seq 1 10)
do
	hap=`expr $hap + $i`
	echo "i=$i -> $hap"
done

echo "1부터 10까지의 합은 $hap"
exit 0
