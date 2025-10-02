#!/bin/bash

# 폴더 삭제 예제
language="Korea English Japan"

# 각 문자열 별로 3개의 폴더가 삭제된다.
rmdir $language

# 하나의 폴더가 삭제: 'Korea English Japan'
rmdir "$language"
