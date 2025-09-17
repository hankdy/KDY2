
l1 = ['DB', 'LG', 'SM', 'LG', 'IBM', '삼성']
l2 = ['DB', 'LG', 'SM', 'LG', 'IBM', '삼성']
l3 = ['DB', 'LG', 'SM', 'LG', 'IBM', '삼성']

print('l1 : ', hex(id(l1)), l1)
print('l2 : ', hex(id(l2)), l2)
print('l3 : ', hex(id(l3)), l3)

l1.clear()
del l2[:]
l3 =[]

print('l1 : ', hex(id(l1)), l1)
print('l2 : ', hex(id(l2)), l2)
print('l3 : ', hex(id(l3)), l3)