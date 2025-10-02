#!/bin/sh

echo "보안전문가가 되는 것이 좋은가요(yes/no)? "
read answer

case "$answer" in
	yes | y | Y | Yes | YES)
		echo "저의 꿈입니다."
		echo "보안 분야는 영원합니다.";;
	[nN]*)
		echo "싫은 이유가 궁금하네요"
		echo "다시 생각해 보세요";;
	*)
		echo "종료합니다."
		exit 1;;
esac

echo "정상종료"
exit 0
