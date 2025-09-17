


# gcounts = {'GLOBAL': 0, 'INFO':0, 'WARN':0}


# %%

def makeAlert(name):
    count = 0
    def alert(message):
        nonlocal count # 외부함수에 선언 지역변수를 사용
        count += 1
        print(f"[{name}] count({count}): {message}")
        
    return alert

# %%


infoAlert = makeAlert("INFO")
warnAlert = makeAlert("WARN")

infoAlert("새로운 사용자 접속을 하였습니다.")
infoAlert("비번이 변경 되었습니다.")

warnAlert("다른 네트워크에서 로그인이 되었습니다.")
warnAlert("로그인이 5번 연속해서 실패했습니다.")

# print('gcounts:', gcounts)
# print("전체 호출 횟수:", gcounts['GLOBAL'])


