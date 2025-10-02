#!/bin/sh

# 변수(num1)에서 100을 할당
num1=100

# 변수(num2)에 변수(num1) 값 100과
# 문자열(+200)이 할당
num2=$num1+200

echo '$num1 -> ' $num1           # 100
echo 'num2=num1+200 -> ' $num2  # 100+200

# 숫자 계산: +, -, *, /
# 역따옴표(`, backtick)로 감싸고 expr 표현식을 써야 한다.
num3=`expr $num1 + 200`
echo 'num3=`expr $num1 + 200` -> ' $num3 # 300

# 연산우선순위 지정을 위해 괄호에 역슬래시(\)를 붙여야 한다.
# 예외: 곱하기(*)는 역슬래시(\)를 붙여야 한다.
num4=`expr \( $num1 + 200 \) / 10 \* 2`
echo 'num4=`expr \( $num1 + 200 \) / 10 \* 2` -> ' $num4 # 결과: 60
exit 0
