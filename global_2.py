
gcount = 0

# %%

def makeAlert(*name):
    def alert(*message):
        global gcount
        gcount += 1
        print(f"[{name}] gcount({gcount}): {message}")


    return alert

# %%


infoAlert = makeAlert("INFO", "DESK")
warnAlert = makeAlert("WARN")

infoAlert("눈길을 주의하세요.", "눈이 많이 와요")
infoAlert("빗길을 조심하세요.")

warnAlert("공사중, 도로끝")
warnAlert("홍수로 도로소실!!!")