a1 = "881229-1234567"

print(a1[:6]) # 앞자리
print(a1[:-8]) # 앞자리

print(a1[7:]) # 뒷자리
print(a1[-7:]) # 앞자리

#%%

number = "031-123-5678"

print(number[:3]) # 국번
print(number[:-9]) # 국번

print(number[4:7]) # 가운데번호
print(number[-8:-5]) # 가운데번호

print(number[8:]) # 끝번호
print(number[-4:]) # 끝번호


#%%

number1 = "02-123-5678"

print(number1[:2]) # 국번
print(number1[:-9]) # 국번

print(number1[3:6]) # 가운데번호
print(number1[-8:-5]) # 가운데번호

print(number1[7:]) # 끝번호
print(number1[-4:]) # 끝번호

#%%

number2 = "010-1234-5678"

print(number2[:3]) # 국번
print(number2[:-10]) # 국번

print(number2[4:8]) # 가운데번호
print(number2[-9:-5]) # 가운데번호

print(number2[9:]) # 끝번호
print(number2[-4:]) # 끝번호

#%%

s3 = number2.split('-')
print(f"{s3}: {s3[0]}.{s3[1]}.{s3[2]}")