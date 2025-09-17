# 튜플(tuple)

# 불변(immutable) 상수 리스트(list)
# 불변 : 요소의 값을 변경할 수 없다.
# 수정(추가, 삭제, 변경)을 할 수 없다.
# 그 외에는 리스트와 비슷하다
# 장점:
#     - 리스트에 비해서 속도가 빠르다.
#     - 공간절약(메모리)
# 특징 : 
#     - 딕셔너리(dict) 키로 활용
#     - 함수(function) dml dlswkfh tkdyd
# 사용 : 
#     - 요소가 한 개인 경우에는 마지막 요소 뒤에 콤마(,)를 붙여야 한다.
#     - 튜플 변수 = (값,)
#     - 튜플 변수 = (값, 값)
    
# 튜플 객체 생성
#     - tuple()
#     - 소괄호 : ()
#     - 소괄호 생략 가능

#%%    
    

# 빈 튜플

t0 = ()
te = tuple()

print(type(t0), t0)
print(type(te), te)

#%%

# 주의 : 요소가 1개인 경우 요소 뒤에 콤마(,) 를 붙여야 한다.

t1a = 1,
t1b = (9,)
print(type(t1a), t1a)
print(type(t1b), t1b)

#%%

# 요소가 2개 이상인 경우에는 콤마를 붙이지 않아도 된다.

t2a = 1,2
t2b = (1,2)
print(type(t2a), t2a)
print(type(t2b), t2b)

#%% 

# 요소의 값을 변경할 수 없다.

tp = (10, 20, 30)

print(tp[0])
print(tp[1])
print(tp[2])

print(id(tp), tp)

#%%

# 요소의 값을 변경할 수 없다.

# tp[0] = 99,


#%% 

jobs = ('요리사', '교사', '사무원')

print(jobs)

# 언패킹(unpacking)
# 언패킹된 변수는 개별 요소의 자료형이다. 

chef, teacher, officer = jobs

print(type(chef), chef)
print(type(teacher), teacher)
print(type(officer), officer)

#%%

a = 1,

one, = a

print(type(one), a)


#%%

tp = (1, 3, 5, 7, 9)

tv = 10 # 바뀔 값

tx = 2 # 바뀔 위치


ty = tp[0:2]  #(1, 3)
ti = 10,
tz = tp[3:]  #(7, 9)

to = ty + ti + tz  #(1, 3) + 10 + (7, 9)

print(to)   


