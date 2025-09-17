
# 파라미터
# what: 문자열
# func : 함수
# vals :  가변인자

def calc(what, func, *vals):
    print(f"calc({what}): ", func(*vals))
    
    
#%%

def add(*vals):
    tot = 0
    for val in vals:
        tot += val
    return tot

fun = add

print("add type: ", type(add))
print("fun type: ", type(fun))


print("add:", add(1,2,3,4,5))
print("fun:", fun(1,2,3,4,5))

#%%

calc("홀수", add, 1,3,5,7,9)
calc("짝수", fun, 2,4,6,8,10)