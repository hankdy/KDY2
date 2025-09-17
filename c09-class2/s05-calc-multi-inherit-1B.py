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
   
"""

#%%

class Calp:
    def __init__(self, val=0):
        self.tot = val
        self.cnt = 0
        
    def count(self):
        self.cnt += 1        

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
        
    def total(self):
        return self.tot
    
    def avg(self):
        return self.tot / self.cnt
    
#%%

calc = Calc()    
calc.add(10) # 10
calc.sub(6)  # 4
calc.mul(3)  # 12
calc.div(3)  # 4.0

print(f"총점={calc.total()}, 평균={calc.avg()}") # 4.0, 1.0

#%%

calc = Calc(10)    
calc.sub(6)  # 4
calc.add(10) # 14
calc.mul(2)  # 28
calc.div(4)  # 7.0

print(f"총점={calc.total()}, 평균={calc.avg()}") # 7.0, 1.75

