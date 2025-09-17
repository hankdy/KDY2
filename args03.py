def tots(title, *vals):
    print(f"[{title}] {vals}", end = ":")
    tot = 0
    for val in vals:
        tot += val
    return tot

#%%

print(tots("홀수", 1,3,5,7))
print(tots("짝수", 2,4,6,8,10))

