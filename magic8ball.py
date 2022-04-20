import random
question = input("")
num = random.randint(1,10)
print(int(num))
if num >= 7:
    print(" It is certain.")
elif num >= 4 and num < 7:
    print(" Cannot predict now.")
else:
    print("My sources say no.")
