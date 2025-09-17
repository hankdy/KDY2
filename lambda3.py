

def calc(what, func, *vals):
    print(f"calc({what}): ", func(*vals))
    
#%%

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b


#%%

calc("덧셈", add, 10, 20)
calc("뺄셈", sub, 10, 6)
calc("곱셈", mul, 10, 3)

#%%

calc("덧셈", lambda a, b: a + b, 10, 20)
calc("뺄셈", lambda a, b: a - b, 10, 6)
calc("곱셈", lambda a, b: a * b, 10, 3)
    
    

    
