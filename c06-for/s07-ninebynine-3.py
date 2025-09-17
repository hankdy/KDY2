# 반복문(for)
# 구구단
#%%

# [문제2] 구구단을 출력하라.
# 2단부터 9단까지 출력하는데 2개 단 단위로 출력하다.

#%%

ds = 2 # 시작 단
de = 9 # 종료 단
dl = 2 # 한 영역에 출력될 단 수

for x in range(ds,de+1,dl):
    for d in range(dl): # 단 정보 출력
        dx = x + d
        if dx > de:
            break
        ds = f"[{dx}단]"
        print(f"{ds:^14}", end="")
    print()

    for y in range(1, 10): # 단의 값을 출력
        for n in range(dl):
            m = x + n
            if m > de:
                break
            z = m * y
            s = f"[{m}]*[{y}]=[{z:>2}]"
            print(f"{s:^15}", end='')
        print()
       
    print('')


