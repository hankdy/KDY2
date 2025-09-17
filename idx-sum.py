# [문제1]
# 국어, 영어, 수학 , 과학 점수를 가진 변수를 만들고

# 점수는 0점부터 100까지 지정한 후

# 총점과 평균을 구하라.

# 선택: 각 과목의 점수를 난수를 발생해서 지정하라.


# [문제2]
#  위 문제 1을 리스트 자료형으로 바꿔서 처리하라.

# #%%

from random import *

a1 = randint(0,100)
a2 = randint(0,100)
a3 = randint(0,100)
a4 = randint(0,100)


print("국어:" , [a1], "영어:", [a2], "수학:", [a3], "과학:", [a4])

b = a1 + a2 + a3 + a4
c = b / 4
print("총합: " ,b)
print("평균값: " , round(c))
print([[a1, a2, a3, a4], b, round(c)])



#%%

titles = [['국어','영어','수학','과학'], '총점','평균']
scores = [[100,90,70,60],0, 0]

score = scores[0]
scores[1] = sum(score)
scores[2] = scores[1] / len(score)

print("#학생 성적#")
title = titles[0]
for idx, sub in enumerate(title):
    print(f"{sub}: {score[idx]}")
    

print("-------------------")
print(f"{titles[1]}: {scores[1]}")
print(f"{titles[2]}: {round(scores[2],2)}")