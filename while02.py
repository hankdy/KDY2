
one = 100000 # 원금
ma = 10
es = 0.1
# mm = ("{0} * 12 / 0.1".format(one)) # 이자율
asd = 1

while asd <= 10:
    y = one * es
    one += y
    print(f"{asd}, {y}, {one}")
    asd += 1

one = round(one)

print(f"{one}")
    
#%%

interest = 0.1
last = 10
total = 100000
cnt = 1

while cnt <= last:
    cost = total * interest
    total += cost 
    print(f"[cnt={cnt}] cost = {cost}, total = {total}")
    cnt += 1
    
total = round(total)
print(f">>> total = {total}")

#%%


    