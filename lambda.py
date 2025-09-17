def max(a, b):
    return a if a > b else b


a = 10
b = 20
c = max(a, b)

print(f"값 {a}와 {b}중에 큰 값은? {c}")


#%%

lambda_max = lambda a, b: a if a > b else b

x = 99
y = 98
z = lambda_max(x, y)
print(f"값 {x}와 {y} 중에 큰 값은? {z}")


#%%

def max(a, b):
    return a if a > b else b


#%%
max = None
#%%

max(10, 20)