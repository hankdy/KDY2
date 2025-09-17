st = {
      "name" : "홍길동",
      "age" : 28,
      "주소": "한양",
      "생존": False
      }

dk = st.keys()
print(dk)


#%%

lk = list(dk)
print(lk)

#%%

tk = tuple(dk)
print(tk)


#%%

for k in dk :
    print(k)
    
#%%

for k in st.keys():
    print(k)

#%%

for k in dk :
    print(f"[{k}] : {st[k]}")