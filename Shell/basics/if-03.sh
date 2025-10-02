#!/bin/sh

hello="HELLO"
world="WORLD"

# 같은가? 참인가?
if [ $hello = $world ]
then
	echo "'$hello'와 '$world'는 같습니다"
else
	echo "'$hello'와 '$world'는 같지않습니다"
fi

exit 0
