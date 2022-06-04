import random

def guess(x):
    random_number = random.randint(1, x) #Random value from range 1 to user input range x
    guess = 0 #Initialization
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Too low, try again!")
        elif guess > random_number:
            print("Too high, try again!")

    print(f"Correct. The number {random_number} was guessed correctly from the range.") #Instead of using an else we hop out

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high) #Error if low == high
        else:
            guess = low #Can also be high, but they're both unequal so it doesn't make a difference
        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C) from the input?").lower() #Lowercasing the input
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        
    print(f"The computer guessed {guess} correctly!")

computer_guess(10000) #Example, can also be user input