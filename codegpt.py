#Lottozahlen Generator als Python code

import random

def lotto_generator(): 
    lotto_numbers = [] 
    while len(lotto_numbers) < 6: 
        number = random.randint(1, 49) 
        if number not in lotto_numbers: 
            lotto_numbers.append(number) 

    return sorted(lotto_numbers) 


print("Ihre Lottozahlen sind:", lotto_generator())