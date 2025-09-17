import sys

money = False

if money : 
    print("택시를 탄다")
    print('택시 요금을 지불한다.')

else :
    print('걸어 간다')
    
print('목적지에 도착')

#%%

money = input("가진 돈을 입력하세요: ")
money = int(money)

print(f"당신이 가진 돈은 ({money}원)입니다.")


if money >= 5000 :
    print("택시를 타고가라")
    
elif 5000 > money >= 1500 :
    print("버스를 타고 가라")
    
else : 
    print("걸어가라")
    
#%%

money = input("가진 돈을 입력하세요: ")
money = int(money)

# bool 자료형
c5000 = money >= 5000
c1500 = money >= 1500

print(f"당신이 가진 돈은 ({money}원)입니다.")

if c5000 :
    print("택시를 타고 가라")

elif c1500 : 
    print("버스를 타고가라")
    
else :
    print("걸어간다.")
    
    
#%%

money = input("가진 돈을 입력하세요: ")
money = int(money)

print(f"내가 가진 돈은 ({money}원) 입니다.")


if money < 1000 :
    print("수돗물을 마셔라")

elif money < 1500 :
    print("생수를 마셔라")
    
elif money < 3000 :
    print("사이다를 마셔라")
    
else :
    print("커피를 마셔라")
    
#%%



money = input("가진 돈을 입력하세요: ")
money = int(money)


print(f"내가 가진 돈은 ({money}원) 입니다.")

coffy = int(3000)
sida = int(2000)
water = int(1000)

recipt = money - coffy
recipt2 = money - sida
recipt3 =  money - water

if money >= 3000 :
    print("커피를 산다")
    print(f"남은 잔돈은 {recipt}입니다.")

elif money >= 2000:
    print("사이다를 산다")
    print(f"남은 잔돈은 {recipt2} 입니다.")
    
elif money >= 1000:
    print("생수를 산다")
    print(f"남은 잔돈은 {recipt3} 입니다.")
    
else :
    print("그냥 집에 간다")
    
#%%

score = input("점수는 몇 점인가요?")
score = int(score)

print(f"제 점수는 {score}점 입니다.")

if  100 >= score >= 90 :
    print("당신은 a 등급입니다.")
elif 90 > score >= 80 :
    print("당신은 b 등급입니다.")
elif 80 > score >= 70 :
    print("당신은 c 등급입니다.")
elif 70 > score >= 60 :
    print("당신은 d 등급입니다.")
elif score < 60 :
    print("당신은 e 등급입니다.")    
else :
    print("잘못된 점수입니다.")
    
    
#%% 

s = [1,3,5,7,9]

x = 1
b = x in s

if b :
    print(f"리스트 s 에 값 {x}가 있다.")
else:
    print(f"리스트 s 에 값 {x}가 없다.")
    
    
#%%

s = "hello, world "