#!/bin/bash

AUTH_URL="www.example.com/"

echo $AUTH_URL
echo "http://$AUTH_URLlogin.html"  # http://.html

# 중괄호({})로 변수를 지정
# ${AUTH_URL} 형태로 지정
echo "http://${AUTH_URL}login.html"  # http://www.example.com/login.html

exit 0
