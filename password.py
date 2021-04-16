from random import randint

def password(n):
    for x in range(n): 
        print(chr(randint(33, 126)), end='')
    
    print()