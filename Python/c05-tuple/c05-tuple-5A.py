# 튜플(Tuple)

# [문제]
# 튜플(1,3,5,7,9)에서 인덱스 2번째의 값 5를 10으로 바꿔라
# 조건 : 아래의 튜플 변수 tp를 사용하라.
# 힌트: 슬라이싱(slicing)를 이용

tp = (1,3,5,7,9)
tv = 10 # 바뀔 값
tx = 2  # 바뀔 위치

# TypeError: 'tuple' object does not support item assignment
# tp[tx] = tv

# [해결1]
# 튜플을 리스트 객체로 만든 후 다시 튜플 객체로 변환
tl = list(tp)
tl[tx] = tv
tp = tuple(tl)
print(tp) # (1, 3, 10, 7, 9)

# [해결2]
# 튜플만 사용해서 해결
tp1 = tp[:tx]   # (1,3)
tp2 = tp[tx+1:] # (7,9)
tp = tp1 + (tv,) + tp2
print(tp) # (1, 3, 10, 7, 9)

