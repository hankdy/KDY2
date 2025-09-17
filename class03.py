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
    
# 학생(student) 클래스 선언
s1 = student()  # 객체 생성

# %%

s1.name('홍길동')
s1.korean(90)
s1.english(80)
s1.maths(70)
print(s1.score())
print('총점:', s1.total())
print('평균:', s1.avg())