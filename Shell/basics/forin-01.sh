#!/bin/sh

hap=0

for i in 1 2 3 4 5 6 7 8 9 10
do
	hap=`expr $hap + $i`
	echo "i=$i -> $hap"
done

echo "1부터 10까지의 합은 $hap"
exit 0
