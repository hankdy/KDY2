# 문자열 str

# enter = crlf(windows), cr(mac), lf(unix) , \next()
# LF (\n) : 라인피드, 줄바꿈, 다음 줄로 이동
# CR (\r) : 캐리지 리턴, 커서를 맨 앞으로 이동
# FF (\f) : 폼 피드, 다음 페이지

#%%

# 탈출문자(escape character)


# ord() : 문자에 해당하는 값을 리턴
cr = ord('\r') # carriage return
lf = ord('\n') # line feed
ff = ord('\f') # form feed
ht = ord('\t') # horizontal tap
bs = ord('\b') # backspace
sp = ord(' ') # space


print('CR:', cr, hex(cr))
print('LF:', lf, hex(lf))
print('FF:', ff, hex(ff))
print('HT:', ht, hex(ht))
print('BS:', bs, hex(bs))
print('SP:', sp, hex(sp))

#%%
ssl = "안녕하세요? \n 반갑습니다. \n 환영합니다. \n"
print(ssl) 

#%%

ss1 = "안녕하세요?\r반갑습니다.\r환영"
print(ss1) 

#%% 
ss2 = "안녕하세요\n\r반갑습니다.\n\r환영합니다."
print(ss2)


#%%
print("1234567890" * 5)
print("ABC\tDEFGHIJK\tLMNOPQ\tEND")

#%%
print("Backspace:","ABC\b\b\bD") #DBC
print("Backspace:","ABC\b\bD") #ADC
