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
    
# %%
    
s1 = student() #객체 생성

print(s1.score())

#%%

student.score(s1)


# %%

s1.name("홍길동")  # 객체 멤버 메서드에 접근(세터)
s1.korean(90)
s1.english(80)
s1.maths(70)
print(s1.score())