class Student:
    def __init__(self, sid='이름없음', kor=0, eng=0, math=0): # 생성자(constructor)
        print(f"[생성자] {self}")
        self.sid = sid
        self.kor = kor
        self.eng = eng
        self.math = math
        
    def __del__(self): # 소멸자(destructor)
        print(f"[소멸자] {self}")
        
    def name(self, val):
        self.sid = val
    
    def korean(self, val):
        self.kor = val
        
    def english(self, val):
        self.eng = val
        
    def maths(self, val):
        self.math = val
        
    def score(self):
        return self.sid, self.kor, self.eng, self.math
    
    def total(self):
        return self.kor + self.eng + self.math
    
    def avg(self):
        return self.total() // 3 
    
# %%

# 자바(java)
# 상속은 확장의 개념
#class school extends student{}

# %%

# 상속
# 자식은 부모의 속성과 메서드를 상속 받음
# 자식은 pass를 하게 되면 자신의 속성과 메서드가 하나도 없음
# 부모의 속성과 메서드만으로 구성되어 있다. 
class school(Student):
    def __init__(self, name,kor,eng,math):
        print(f"[scool] 생성자: {self}")
        super().__init__(name, kor, eng, math) # 부모 생성자 호출
        
    def score(self):
        print(f"[scool] score")
        return self.sid, self.kor, self.eng, self.math, self.total(),self.avg()
# %%


sc = school()
print(sc.score()) 

# %%

sc = school('전교생')
print(sc.score()) 

