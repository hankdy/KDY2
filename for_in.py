# 반복문 (for)
# for 변수 in 리스트, 튜플, 문자열, ...

lists = ['one', 'two', 'three', 'four']

# 리스트에 들어 있는 내용의 갯수만큼 반복하면서 
# 아이템을 하나씩 꺼내서 변수에 담아준다.

for item in lists:
    print(item)
    
# 반복문
# for 문 : 횟수
# while 문  : 조건

#%%

# range(시작값 / 종료값 / 간격)

#%%

y = {"한글":1, "영어":2, "수학":3}

for x in y:
    print(x)
    


#%% 

lists = [(1,"one"), (2,'two'), (3,'three'),(4, "four")]


for tuples in lists :
    print(type(tuples),tuples,' : ', end = '')
    print(tuples[0],',', tuples[1])
    
    
#%%
for tuples in lists : # 4번 반복
    print(tuples, end='')
print()

#%%
for tuples in lists : # 4번 반복
    for tx in tuples: # 2번 반복
        print(tx,end='')
    print()
    
    

#%%


# printx = print
# printx("hello") # hello"

#%%

lists = [(1,"one"), (2,'two'), (3,'three'),(4, "four")]

for (first, second) in lists:
    print(f"{first},{second}")

#%%

for item in 1,3,5,6, "end!":
    print(item)

#%%

for item in "hello, world":
    print(item)
    
    
#%%

# 국어, 국사, 과학 , 수학의 점수를 튜플로 저장하여 
# 각 과목과 점수를 출력하고 총점, 평균을 구하라.
# 조건 
#  - 평균은 소수점 2자리까지 출력하라. 
#  - 각 과목의 점수는 0부터 100까지 난수로 처리
#  - 총 점은 for 문으로 계산하라.

from random import*

scores = {
    "과목" :{
        "국어": 0,
        "국사": 0,
        "과학": 0,
        "수학": 0
        },
    "총점": 0,
    "평균": 0.0
 }

subject = scores['과목']
# print(subject)


tot = 0
for sub in subject :
    score = randint(0,100)
    subject[sub] = score
    tot += score
    
scores['총점'] = tot

scores['평균'] = round(tot / len(subject), 2)

# scores['최저'] = min(subject,values())

# scores['최고'] = max(subject,values())

for key in scores:
    if key == '과목':
        subs = scores[key]
        for sub, val in subs.items():
            print(f"{sub} : {val}")
        print( '-' * 10 )
    else :
        val = scores[key]
        print(f"{key} : {val}")
        
        
        
#%%



    
