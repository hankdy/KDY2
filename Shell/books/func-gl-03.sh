#!/bin/bash

# Global Variable
language="Korean"

# 함수 정의 안에서 local을 지정하지 않고 변수를 선언하면?
# * 권고하지 않음
function learn() {
	# local를 명시하지 않으면 전역변수가 된다.
	learn_language="English"
	echo "I am learning '$learn_language'"
}

function print() {
	echo "I can speak '$1'"
}

learn                  # I am learning 'English'
print $language        # I am speak 'Korean'
print $learn_language  # I am speak 'English'

