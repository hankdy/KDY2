# 리스트 정렬
# sorted = built - in function


lst = [4, 7, 3, 10, 99, 22]

print(id(lst), lst)

lst.sort()

print(id(lst), lst)


# 정렬

lst_asc = sorted(lst)

print("오름차순: " , id(lst_asc), lst_asc)

lst_desc = sorted(lst, reverse=True)

print("내림차순: " , lst_desc)
