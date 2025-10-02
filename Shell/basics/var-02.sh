#!/bin/sh

# 작은 따옴표로 감싸면 내용은 문자 취급
# 큰 따옴표 안에 $변수는 변수로 취급

hello="Hello World"

echo "따옴표 없음(변수): " $hello
echo "큰따옴표(변수): " "$hello"
echo "작은따옴표(문자):" '$hello'
echo "역슬래시(문자):" \$hello
echo "역슬래시(문자,변수):" \$$hello
echo "큰따옴표와 역슬래시(문자):" "\$hello"
echo "작은따옴표와 역슬래시(문자):" '\$hello'

