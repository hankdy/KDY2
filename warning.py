


gcounts = {'GLOBAL': 0, 'INFO':0, 'WARN':0}


# %%

def makeAlert(name, counts):
    def alert(message):
        counts['GLOBAL'] += 1
        counts[name] += 1
        
        print(f"[{name}] counts({counts[name]}): {message}")
        

            
    return alert

# %%


infoAlert = makeAlert("INFO", gcounts)
warnAlert = makeAlert("WARN", gcounts)

infoAlert("새로운 사용자 접속을 하였습니다.")
infoAlert("비번이 변경 되었습니다.")

warnAlert("다른 네트워크에서 로그인이 되었습니다.")
warnAlert("로그인이 5번 연속해서 실패했습니다.")

print('gcounts:', gcounts)
print("전체 호출 횟수:", gcounts['GLOBAL'])



