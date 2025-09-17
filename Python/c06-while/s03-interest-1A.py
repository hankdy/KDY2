# 반복문(while)

# 예금을 예치하여 복리이자 계산
# 원금 10만원, 이자가 연10%, 만기 10년, 복리로 계산하라.

interest = 0.1  # 이자
last = 10       # 만기(10년)
total = 100000  # 총금액
cnt = 1         # 년도

while cnt <= last:
    cost = total * interest # 이자
    total += cost
    print(f"[cnt={cnt}] cost={cost}, total={total}")
    cnt += 1

total = round(total)
print(f">>> total={total}")

# >>> total=259374


