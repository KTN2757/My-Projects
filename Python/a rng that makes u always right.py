import random

l = [1, 2, 3]
n = random.randint(1, 3)
a = input("Enter a number: ")
while int(a) != int(n):
    n = random.randint(1, 3)
    if int(a) > l[-1]:
        print(f"ENTER A NUMBER BETWEEN {l[0]} and {l[-1]}")
        break
print(n)
