import random

print("hello")

while True:
    toss = random.randint(1, 6)
    print(toss)
    if toss == 6:
        print("congratulation! you have a new chance!")
        new_chance = random.randint(1, 6)
        print(new_chance)

    else:
        break
