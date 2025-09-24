#!/bin/sh

fname=/lib/systemd/system/cron.service
if [ -f $fname ]
then
	head -5 $fname
else
	echo "cron 서버가 설치되어 있지 않습니다."
fi

exit 0
