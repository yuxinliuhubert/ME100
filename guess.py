# Guess the number
import random
terminate = False
count = 0
ans = random.randint(1,15)
while terminate == False:
    n = int(input("Take a guess: "))
    count = count+1
    if n < ans:
         print("Your guess is too low")
    elif n > ans:
        print("Your guess is too high")
    else:
        terminate = True;
        print("Congratulations, you guessed my number in",count,"trials!")
