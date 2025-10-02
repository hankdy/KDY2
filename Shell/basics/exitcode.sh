#!/bin/sh

# exit code 받기

# while-bce-01.sh를 실행하여 exit code 받아 출력하기 
./while-bce-01.sh

# recevie exit code
EXIT_CODE=$?

echo "호출한 셸의 종료 코드는: ($EXIT_CODE)입니다"
