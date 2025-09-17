print(5>10)
print(5<10)

print(True)
print(False)

print(not True)
print(not False)

not (5>10)

print(not(5>10))


#%%

# d = not a  
# f = not b  


#%%

print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 개인데, 이름은 연탄이예요")
print("연탄이는 4살이고, 산책을 아주 좋아해요")
print("연탄이는 수컷인가요?")
print("네")


#%%

name = "연탄이"
animal = "개"
age = 4
hobby = "산책"

print("반려동물을 소개해 주세요")
print("우리 집 반려동물은 "+ animal +" 인데, 이름이 " + name +"예요.")
print(name + "는" + str(age) +"살이고," + hobby + "을 아주 좋아해요")

#%%

name = "해피"
animal = "고양이"
age = 4
hobby = "낮잠"

print("반려동물을 소개해 주세요")
print("우리 집 반려동물은 "+ animal +" 인데, 이름이 " + name +"예요.")
print(name + "는" + str(age) +"살이고," + hobby + "을 아주 좋아해요")

print(f"우리 집 반려동물은 {animal} 인데, 이름이 {name} 예요.")
print(f"{name}은 {age}살이고 {hobby}를 아주 좋아해요")

print("우리 집 반려동물은 %s 인데, 이름이 %s 예요"%(animal,name))
print("%s 는 %d 살이고 %s 을 좋아해요"%(name,age,hobby))

print("우리 집 반려동물은 {0} 인데, 이름이 {1} 예요".format(animal,name))


#%%

animal = 개
name = 몽실이
age = 4
hobby = 산책
sex = 수컷

print(f"몽실이는 {sex}입니다.")


