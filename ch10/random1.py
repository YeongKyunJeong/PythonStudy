# random1.py

import random

animals = ["체셔고양이", "오리", "도도새", "호랑이", "고래"]

print(random.choice(animals))
print(random.choice(animals))
print(random.choice(animals))

print("-------------------------")
print(random.sample(animals, 3))

print("-------------------------")
print(random.randint(1, 2))
print(random.randint(1, 100))


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(random.choice(numbers[:5]))
print(random.choice(numbers[:5]))
print(random.choice(numbers[:5]))