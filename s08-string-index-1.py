
tel = "010-1234-5678"
tfs = '-'

s1 = tel.find(tfs)
t1 = tel[:s1]

s2 = tel.find(tfs, s1+1)
t2 = tel[s1+1:s2]

s3 = tel.find(tfs, s2+1)
t3 = tel[s2+1:s3]

print(t1)
print(t2)
print(t3)

#%%

s = "python is the best choice"


ss = s
fs = ' '
sx = -1

while True :
    sn = sx + 1
    print("시작위치:", sn)
    ss = ss[sn:]       #0,
    sx = ss.find(fs)
    if sx == -1:
        sw = ss[:]
        print(sw)
        break
    
    sw = ss[:sx]
    print(sw)
    


    
