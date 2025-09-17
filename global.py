# # -*- coding: utf-8 -*-
# """
# Created on Tue Sep  9 10:47:26 2025

# @author: kangde
# """

# def sum(a, b):
#     print(f"{a} 더하기 {b} = {a + b}")
#     print(f"{a} 뺴기 {b} = {a - b}")   
#     print(f"{a} 곱하기 {b} = {a * b}")   
#     print(f"{a} 나누기 {b} = {a / b}")    
#     print(f"{a} 제곱근 {b} = {a ** b}")
 
    

# sum(4, 5)
    
# #%%


# class Calculator:
#     def __init__(self):
#         return power 
#         self.result = 0
#         self.history = []

#     def add(self, value):
#         self.result += value
#         self.history.append(f"Add {value} => {self.result}")
#         return self.result

#     def subtract(self, value):
#         self.result -= value
#         self.history.append(f"Subtract {value} => {self.result}")
#         return self.result

#     def multiply(self, value):
#         self.result *= value
#         self.history.append(f"Multiply by {value} => {self.result}")
#         return self.result

#     def divide(self, value):
#         if value == 0:
#             self.history.append("Divide by 0 => Error")
#             raise ValueError("0으로 나눌 수 없습니다.")
#         self.result /= value
#         self.history.append(f"Divide by {value} => {self.result}")
#         return self.result

#     def modulo(self, value):
#         self.result %= value
#         self.history.append(f"Modulo {value} => {self.result}")
#         return self.result

#     def power(self, value):
#         self.result **= value
#         self.history.append(f"Power of {value} => {self.result}")
#         return self.result

#     def total(self):
#         return self.result

#     def average(self):
#         if not self.history:
#             return 0
#         numbers = [float(line.split("=>")[1]) for line in self.history if "=>" in line and "Error" not in line]
#         return sum(numbers) / len(numbers)

#     def show_history(self):
#         print("---- 계산 이력 ----")
#         for item in self.history:
#             print(item)
#         print("-------------------")
        

#%%

# 전역변수 (global variable)
historys = []
totals = []
total = 0
count = 0

#%%

def plus(a, b):
    return a + b

#%%

def sub(a, b):
    return a - b

#%%

def div(a, b):
    return a // b

#%%
def mul(a, b):
    return a * b

#%%

def sur(a, b):
    return a % b

#%%

def pow(a, b):
    return a ** b

#%%

def calc(a, op, b):
    if op == '+' :
        c = plus(a, b)
    elif op == '-':
        c = sub(a, b)
    elif op == '/':
        c = div(a, b)
    elif op == '*':
        c = mul(a, b)
    elif op == '%':
        c = sur(a, b)
    elif op == '**':
        c = pow(a, b)
    else :
        return 0
    
    
    # global을 선언하지 않고 전역변수를 수정하려고 하면 로컬변수에서 찾음
    global total
    global count
    global totals
    
    count += 1
    total += c
    totals.append(c)
    return c

#%%

def tot():
    return total

def avg():
    return total / count


#%%

calc(10, '+', 20)
calc(2, '*' , 4)
calc(10,'/',2)
calc(2, '**', 3)


print("총합:" , tot())
print("평균:", avg())
print(total)
        
