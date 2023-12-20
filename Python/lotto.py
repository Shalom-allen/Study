# 로또복권
import random

for j in range(5):
    lotto_number = []
    
    for i in range(1,7):
        number = list(range(1,46))
        my_choice = random.choice(number)
        
        while my_choice in lotto_number:
            my_choice =random.choice(number)
            
        lotto_number.append(my_choice)
    
    print(lotto_number)


