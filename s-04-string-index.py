s = "Python is the best choice"
fs = ' '
sx = 0

while True :
    se = s.index(fs, sx)
    ss = s[sx:se]
    print(ss)
    sx = se + 1
    

#%%

# 예외처리

s = "Python is the best choice"
fs = ' '
sx = 0



while True:
    try:
        se = s.index(fs, sx)
        ss = s[sx:se]
        sx = se + 1
        print(ss)
    except :
        print(s[sx:])
        break