#!/bin/sh

printx() {
	echo "printx: $1"
}

printx
printx Hello
printx World

# 하나의 인자로 전달하려면 따옴표로 묶어야 한다.
printx "Hello World"
printx 'Welcome to Shell!'

# 따옴표로 묶지 않으면 공백으로 분리되어 전달된다.
# 아래의 인자는 3개가 전달되면 printx는 1개만 처리한다.
printx one two three
