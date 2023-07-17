import math

p = input("Perpendicular: ")
b = input("Base: ")
h = input("Hypotenuse: ")
if h == "?":
    h = math.sqrt(float(p) ** 2 + float(b) ** 2)
    print(h)
elif p == "?":
    p = math.sqrt(float(h) ** 2 - float(b) ** 2)
    print(p)
elif b == "?":
    b = math.sqrt(float(h) ** 2 - float(p) ** 2)
    print(b)
else:
    print("All the side are already there")
