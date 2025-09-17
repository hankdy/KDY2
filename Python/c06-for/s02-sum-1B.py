# 반복문(for)

"""
# [문제]
# 국어, 국사, 과학, 수학의 점수를 딕셔너리(dict)로 저장하여
# 각 과목과 점수를 출력하고 총점, 평균을 구하라.
# 각 과목에서 최저 점수와 최고 점수를 표시하라.
# 조건: 
#   - 각 과목의 점수는 0부터 100까지 난수로 처리하라.
#   - 총점은 for문으로 계산하라.
#   - 평균은 소숫점 2자리까지 출력하라.
"""
#%%

from random import randint

scores = {
    "과목": {
        "국어": 0,
        "국사": 0,
        "과학": 0,
        "수학": 0,
    },
    "총점": 0,
    "평균": 0.0
}

# '과목'에 해당하는 딕셔너리
# 디셔너리를 참조하여 수정하면 원본에 반영
subject = scores['과목']

# 점수 할당 및 총점
tot = 0
for sub in subject: # 딕셔너리의 키을 얻음
    score = randint(0, 100) # 0부터 100까지 난수
    subject[sub] = score    # 각 과목에 점수 할당
    tot += score            # 총점 계산
        
# 총점
scores['총점'] = tot

# 평균 : 총점 / 과목수 -> 소숫점 2자리에 반올림
scores['평균'] = round(tot / len(subject), 2)

# 최저
scores['최저'] = min(subject.values())

# 최고
scores['최고'] = max(subject.values())
    
# 출력
for key in scores:   # 딕셔너리의 키을 얻음
    if key == '과목':
        subs = scores[key]
        for sub, val in subs.items():
            print(f"{sub} : {val}")
        print('-' * 10)
    else:
        val = scores[key]
        print(f"{key} : {val}")
            
