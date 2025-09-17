def move(**kwargs):
    print(f"[move] type:{type(kwargs)}, {kwargs}")
    for key in kwargs.keys():
        print(f"key={key}, value= {kwargs[key]}")
        
    

# 호출할 떄 반드시 인자에 파라미터를 명시해야 한다.

move(x=10, y=20)

move(Z=15, i=10)

move(x=10, y=20, z=30)


