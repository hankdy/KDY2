ss = "Python is the best choice"
sp = ss.split()

print("-" *30)
for item in sp :
    print(item)
    

print('-' * 30)
for idx,item in enumerate(sp):
    print(f"sp[{idx}] : {item}, {sp[idx]}")