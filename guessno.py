import random 
secret = random.randint(1,10)
guess=0
while guess != secret:
    guess = int(input("Guess any no from 1 to 10:"))
    if guess<secret:
        print("Value too low ")
    elif guess>secret:
        print("Value too high ")
else:
    print("Guess is correct",secret)