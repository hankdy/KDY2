

# def move(x, y, z):
#     print(f"x = {x}, y = {y}, z = {z}")

# #%%


# # 함수 호출
# # 순서 대로 인자를 지정
 
# move(10, 20, 30)

#%%

"""
기본값: default value
파라미터 : z의 기본값은 5
호출 할때 값을 전달하지 않으면 기본값으로 처리

"""

def move(x, y, z=5):
    print(f'move"x({x}), y({y}), z({z})')
    
    
#%%

move(10, 20)

#%%
move(10, 20, 30)

#%%
move(x = 1, y = 2, z = 3)