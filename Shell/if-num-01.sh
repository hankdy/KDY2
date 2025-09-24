#!/bin/sh

# -eq : EQual
if p 100 -eq 200 ]
then
	echo '100과 200은 같다.'
else
	echo '100과 200은 다르다.'
fi
exit 0
