#!/bin/bash

# Global Variable
language="Korean"

# 지역변수는 함수 안에서 선언된 변수로서
# 함수가 종료되면 사라지는 변수이다.
# 그러므로 함수 밖에서는 참조할 수 없다.
# 지역변수: local learn_language="English"
function learn() {
	# 지역변수(local variable) 선언
	local learn_language="English"
	echo "I am learning '$learn_language'"
}

function print() {
	echo "I can speak '$1'"
}

learn                  # I am learning 'English'
print $language        # I am speak 'Korean'
print $learn_language  # I am speak ''

