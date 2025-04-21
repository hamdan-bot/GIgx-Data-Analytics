# rolling dice game
import random
while True:
 x=input('want to roll the dice (y/n):').lower()
 if x == 'y' :
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    print(f'({die1},{die2})')
 elif x == 'n' :
    print("thanks for playing!!")
    break
 else :
    print("invalid choice!")