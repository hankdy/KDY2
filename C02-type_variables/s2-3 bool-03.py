a = "홍길동"
b = "전우치"
c = (a == b)
d = (a is b)
e = (a != b)
f = (not a is b)

print('a:', a, type(a))
print('b:', b, type(b))
print('c:', c, type(c))
print('d:', d, type(d))
print('e:', e, type(e))
print('f:', f, type(f))

#%%

animal = "개"
name = "몽실이"
age = 4
hobby = "산책"
sex = "수컷"

print(input("반려동물을 소개해주세요"))
print("우리 집 반려동물은 %s 인데 이름은 %s 예요"%(animal,name))

print(input("나이와 취미가 어떻게 되나요?"))
print(f"{name}은 {age}살이고 {hobby}를 아주 좋아해요")
print("{0}는 밤마다 {1} 가자고 난리입니다.".format(name,hobby))

print(input("몽실이는 성별이 어떻게 되나요?"))
print(f"몽실이는 {sex}입니다.")

print(input("몽실이는 몇살인가요?"))
print(f"우리집 개는 사람나이로 치면 {int(age*5.6)}살 입니다.")


#%%
dog_name = input("개 이름을 입력하세요: ")
dog_age = int(input("개 나이를 입력하세요: "))
dog_gender = input("개 성별을 입력하세요(암/수):")
dog_hobby = input("개의 취미를 입력하세요: ")

human_age = int(dog_age * 5.6)

print("\n ======입력하신 결과======")
print("개 이름:",dog_name)
print("개 나이:",dog_age)
print("개 성별:",dog_gender)
print("개 취미:",dog_hobby)
print("사람 나이로 환산하면 :",human_age)


#%%

dog = input("강아지의 이름, 나이, 성별, 취미를 가르켜주세요:")
dogs = dog.split(",")
print(type(dogs),dogs)

dog_name = dogs[0]
dog_age =  dogs[1]
dog_gender = dogs[2]
dog_hobby = dogs[3]

print("\n ======입력하신 결과======")
print("개 이름:",dog_name)
print("개 나이:",dog_age)
print("개 성별:",dog_gender)
print("개 취미:",dog_hobby)
print("사람 나이로 환산하면 :",human_age)
