  
# number guessing game
import random
number_to_guess=random.randint(1,100)
while True:
  try:
    guess=int(input(f"guess a number b/w 1 to 100 :"))
        
    if guess < number_to_guess:
            print("too low!")
    elif guess > number_to_guess:
            print("too high!")
    else:
            print(f"congratulations! you guessed the number rightly.")
            break
  except ValueError:
             print("invalid input! please enter a integer.")
    
        
    