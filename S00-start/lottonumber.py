import random

def generate_lotto_numbers():
    return sorted(random.sample(range(1, 46), 6))

# 사용 예시
lotto_numbers = generate_lotto_numbers()
print("이번 주 로또 번호:", lotto_numbers)


