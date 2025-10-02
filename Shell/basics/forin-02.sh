#!/bin/bash

# bash SHELL에서만 가능
# for ((i=1; i<=10; i++))
# bash forin-02.sh

hap=0

for ((i=1; i<=10; i++))
do
	hap=`expr $hap + $i`
	echo "i=$i -> $hap"
done

echo "1부터 10까지의 합은 $hap"
exit 0
