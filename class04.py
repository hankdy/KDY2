class student:
    def __init__(self):   # 생성자 (constructor)
        # 속성    
        self.sid = '이름없음'
        self.kor = 0
        self.eng = 0
        self.math = 0
        
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
        # return total() / 3
        return round(self.total() / 3)
    
    
# %%


s1 = student()
s1.name('홍길동')

s2 = student()
s2.name('강감찬')

# 권장하지 않음
# 객체의 속성값을 접근하여 변경 가능
s1.sid = '고길동'
s2.sid = '고길동'

print('s1:', s1.sid)
print('s2:', s2.sid)

print("s1 == s2", s1 == s2)

# %%

print(type(s1), hex(id(s1)), s1)
print(type(s2), hex(id(s2)), s2)
