import random

rendomnum = random.randrange(0,9)

num = rendomnum
chance = 0
while chance < 3:
    ask = int(input("guess: "))
    if ask == num:
        print("you won!")
        break
    chance = chance + 1
else:
    print("you faild!")
    print(f"real number was {num}")
