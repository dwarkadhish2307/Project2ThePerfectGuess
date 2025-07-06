import random
n = random.randint(1, 100)
a = -1
guesses = 0
while(a != n):
    guesses += 1
    a = int(input("Guess the number:"))
    if(a >n):
        print("Lower number please")
        guesses += 1
    else:
        print("Higher number please")
        guesses += 1

print(f"You have guessed the number correctly in{guesses} attempt")
