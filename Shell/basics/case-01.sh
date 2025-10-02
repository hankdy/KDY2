#!/bin/sh

# 다중선택: case ~ esac
# 파라미터: start, stop, restart

case "$1" in
	start)
		echo "작업시작...";;
	stop)
		echo "작업중지...";;
	restart)
		echo "재시작...";;
	*)
		echo "디폴트...";;
esac

echo "작업종료"

exit 0
