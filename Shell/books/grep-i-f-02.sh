#!/bin/bash

echo "^\[[[:alnum:]]*\]" > patternx.txt
grep -i -f ./patternx.txt ./expression2.txt

echo "---------------------------------------------------"
echo "option: --color"
grep --color -i -f ./patternx.txt ./expression2.txt

echo "---------------------------------------------------"
echo "option: --color"  # 매칭된 값을 컬러로 표시
echo "option: -o"       # 매칭된 값만 출력
grep --color -o -i -f ./patternx.txt ./expression2.txt
