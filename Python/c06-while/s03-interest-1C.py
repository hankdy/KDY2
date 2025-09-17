# 반복문(while)

# 예금을 예치하여 계산
# 원금 10만원, 이자가 연10%, 만기 10년, 이자 계산하라.

interest = 0.12 # 이자
last = 10       # 만기(10년)
total = 100000  # 총금액
cnt = 1         # 년도
costot = 0      # 총이자

while cnt <= last:
    cost = total * interest # 이자
    costot += cost
    # print(f"[cnt={cnt}] cost={cost}, total={costot}")
    cnt += 1

total += costot
print(f">>> 총이자={costot}")

# >>> 총이자=120000.0


