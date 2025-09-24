#!/bin/sh

# 변수:
#   - 변수에 할당하는 값은 모두 문자열로 취급
#   - 할당연산자(=) 좌우에는 공백이 없어야 한다.
#   - 대소문자 구분한다.
#   - 변수 할당: 변수=값
#   - 변수 참조: $변수

# 변수에 값을 할당할 때는 공백이 있으면 안된다.
valx = Hello

# 정상: 문자열로 취급
val1=Hello

# 정상적으로 처리되지 않음: 공백처리 됨
val2=Yes Sir

# 권고: 문자열 사이에 공백이 있으면 큰따옴표로 감싸야 한다.
val3="Yes Sir"

# 연산을 수행하지 않고 문자열로 취급
val4=7+5

# 출력 결과
echo "valx:" $valx  # valx:
echo "val1:" $val1  # val1: Hello
echo "val2:" $val2  # val2:
echo "val3:" $val3  # val3: Yes Sir
echo "val4:" $val4  # 7+5
echo "THE END"
