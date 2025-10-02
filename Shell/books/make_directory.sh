#!/bin/bash

# 폴더 생성 예제
language="Korea English Japan"

# 각 문자열별로 3개의 폴더가 생성된다.
mkdir $language

# 하나의 폴더가 생성: 'Korea English Japan'
mkdir "$language"
