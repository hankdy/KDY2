

x = 10
y = 3

print(f"{x} * {y} ->", (lambda a, b : a * b)(x, y))
print(f"{x} ** {y} ->", (lambda a, b : a ** b)(x, y))

#%%

a = 30
b = 40
c = 10
r = lambda a, b, c :a if a > b and a > c else b if b > c and b > c else c 

print(f"{a} ,{b}, {c} 중에 가장 큰 값은?", r(a,b,c))

#%%
a = 30
b = 40
c = 10

r = lambda *new :a if a > b and a > c else b if b > c and b > c else c 

print(f"{a} ,{b}, {c} 중에 가장 큰 값은?", r(a,b,c))