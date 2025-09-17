# -*- coding: utf-8 -*-

# 함수(Function)

#%%
# [문제]
# 국어, 영어, 수학의 점수를 받아서 총점과 평균을 구하는 함수를 각각 정의하라.
# 그리고 함수를 호출해서 결과를 출력하라.

#%%

# 총점 : 국어, 영어, 수학과목의 점수를 인자로 받음
def total(k, e, m):
    return k + e + m

# 평균 : 총점, 과목수
def average(tot, cnt):
    return tot / cnt

#%%

tot = total(70,80,90)
avg = average(tot, 3)
print("총점:", tot)
print("평균:", avg)

    

