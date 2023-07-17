numbers = []
numberOfNumbers = int(input("How many numbers? "))
for i in range(0, numberOfNumbers):
    i += 1
    if i == 1:
        n = int(input(f"Enter the {i}st number: "))
    elif i == 2:
        n = int(input(f"Enter the {i}nd number: "))
    elif i == 3:
        n = int(input(f"Enter the {i}rd number: "))
    else:
        n = int(input(f"Enter the {i}th number: "))
    numbers.append(n)
print(numbers)
average = (sum(numbers)) / numberOfNumbers
print(average)
