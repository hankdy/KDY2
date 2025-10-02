#!/bin/bash

language="Korean"

echo "global variable: $language"

function printx() {

	echo "I can speak $language"
}

printx
