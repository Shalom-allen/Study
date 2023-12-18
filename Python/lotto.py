# 로또복권
import random

lotto_number = []
number = list(range(1,46))

for i in range(1,7):
    my_choice = random.choice(number)
    lotto_number.append(my_choice)

print(lotto_number)
