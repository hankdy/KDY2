#!/bin/bash

# Global Variable
language="Korean"

function print() {
	# 함수 안에서 전역변수를 참조
	echo "I can speak '$language'"
}

print
