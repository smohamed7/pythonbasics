import random
random_num = random.randint(1,21)
start = 1

while start <=5:
    guess = int(input("Guess a number:"))
    if random_num!=guess:
        print("wrong! try again")
        start!=1

    else:
        print("yeess!!!correct")
        break