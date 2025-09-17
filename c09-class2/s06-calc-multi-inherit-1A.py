# -*- coding: utf-8 -*-

"""
# [전자] 전자계산기
1. 다중 상속을 이용하라.
2. 사칙연산을 수행하는 클래스를 각각 정의
   - 덧셈 클래스
   - 뺄셈 클래스
   - 곱셈 클래스
   - 나눗셈 클래스
3. 최하위 클래스에서 다중상속을 하여 통합
   - 총점, 평균 처리
4. 각 클래스들은 생성자 정의하여 초깃값을 넣어라.   
5. 히스토리를 관리하라.
"""

#%%

class Calp:
    def __init__(self, val=0):
        self.svl = val
        self.clear()
        
    def count(self):
        self.cnt += 1        

    def clear(self):
        self.tot = self.svl
        self.cnt = 0
        

#%%

class Plus(Calp):
    def __init__(self, val):
        super().__init__(val)
    
    def add(self, val):
        self.count()
        self.tot += val
        return self.tot
    

#%%

class Minus(Calp):
    def __init__(self, val):
        super().__init__(val)
    
    def sub(self, val):
        self.count()
        self.tot -= val
        return self.tot

#%%

class Multiply(Calp):
    def __init__(self, val):
        super().__init__(val)
    
    def mul(self, val):
        self.count()
        self.tot *= val
        return self.tot

#%%

class Divide(Calp):
    def __init__(self, val):
        super().__init__(val)
    
    def div(self, val):
        self.count()
        self.tot /= val
        return self.tot

#%%

class Calc(Plus, Minus, Multiply, Divide):
    def __init__(self, val=0):
        super().__init__(val)
        self.histories = [] # 이력처리
        
    def total(self):
        return self.tot
    
    def avg(self):
        return self.tot / self.cnt
    
    def comp(self, op, val):
        if op == '+':
            return super().add(val)
        elif op == '-':
            return super().sub(val)
        elif op == '*':
            return super().mul(val)
        elif op == '/':
            return super().div(val)
        
    # 재계산(히스토리)
    def recalc(self): 
        self.clear()
        for op, val in self.histories:
            self.comp(op, val)
    
    def save(self, op, val):
        self.histories.append((op, val)) # 히스토리에 보관
       
    def add(self, val):
        self.save('+', val)
        return super().add(val)
                
    def sub(self, val):
        self.save('-', val)
        return super().sub(val)
    
    def mul(self, val):
        self.save('*', val)
        return super().mul(val)
            
    def div(self, val):
        self.save('/', val)
        return super().div(val)
    
    def history(self):
        for op, val in self.histories:
            print(f"op({op}), val({val})")

    
#%%

calc = Calc()    
calc.add(10) # 10
calc.sub(6)  # 4
calc.mul(3)  # 12
calc.div(3)  # 4.0
print(f"계산: 총점={calc.total()}, 평균={calc.avg()}")

calc.history()
calc.recalc()
print(f"검산: 총점={calc.total()}, 평균={calc.avg()}")

