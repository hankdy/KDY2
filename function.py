def calc(name):
    histories = []
    total = 0
    count = 0
    
    def tot():
        nonlocal total
        return total
    
    def avg():
        nonlocal total, count
        # nonlocal count
        return total / count
    
    def recalc():
        nonlocal histories
        
        t = 0
        for a, op , b in histories:
            c = comp(a, op, b)
            t += c
            print(f"{c} = {a} {op} {b} : total({t})")
        return t, t / len(histories) # 튜플(총합, 평균)
    
    def compute(a, op, b):
        nonlocal total, histories, count
        # nonlocal histories
        # nonlocal count
        
        c = comp(a, op, b)
        if c == None :
            return 0
        
        count += 1                  # 연산횟수 누적
        total += c                  # 연산결과 누적
        histories.append((a,op,b))  # calc() 함수에 전달된 인자를 보관(튜플)
        return c                    # 단위연산 결과 리턴
    
    def calc(oper, *args):
        if oper == 'tot':
            return tot()
        elif oper == 'avg':
            return avg()
        elif oper == 'recalc':
            return recalc()
        elif oper == 'calc':
            a, op, b = args
            return compute(a, op, b)
        else:
            return None
        
    return calc

#%%
# 더하기
def plus(a, b):
    return a + b

# 빼기
def sub(a, b):
    return a - b

# 곱하기
def mul(a, b):
    return a * b

# 나누기(정수 나누기)
def div(a, b):
    return a // b

# 나머지
def sur(a, b):
    return a % b

# 제곱
def pow(a, b):
    return a ** b
        

# %%


def comp(a, op, b):
    if op == '+':
        c = plus(a, b)
    elif op == '-':
        c = sub(a, b)
    elif op == '*':
        c = mul(a, b)
    elif op == '/':
        c = div(a, b)
    elif op == '%':
        c = sur(a, b)
    elif op == '**':
        c = pow(a, b)
    else: # 준비되지 않은 연산자
        return None
    
    return c

# %%

calc = calc("전자계산기")
calc('calc',10, '+', 20)      # 30    
calc('calc',2,  '*', 4)       # 8
calc('calc',10, '/', 2)       # 5
calc('calc',2,  '**', 3)      # 8


print("총합:", calc('tot'))  # 51 
print("평균:", calc('avg'))  # 12.75 
print("검산:", calc('recalc'))  # (51, 12.75)

