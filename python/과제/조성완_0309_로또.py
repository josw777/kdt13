import random

lotto = random.sample(range(1,46),6)
print("**오늘의 행운의 숫자**")
for i, num in enumerate(lotto,1):
    print(f"{i}번째 숫자는: {num}")