#!/bin/sh

# 반복문에서 탈출 및 계속
# break: 반복문을 탈출
# continue: 반복문의 조건식으로 이동하여 아래의 실행을 건너 뜀
# exit: 프로그램을 완전 종료

# 무한루프
while [ 1 ] ; do
	echo -n "[무한반복] (b:break, c:continue, e:exit) ? "
	read input
	case $input in
		b | B)
			echo "루프탈출..."
			break;;
		c | C)
			echo "조건식으로 돌아감(continue)"
			continue;;
		e | E)
			echo "프로그램 종료(exit)"
			exit 1;; # 숫자 one(1)
	esac
done

echo "작업종료"
exit 0
