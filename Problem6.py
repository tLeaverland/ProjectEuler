def sumSquareDif():
    num1 = 0
    num2 = 0
    for i in range(1,101):
        num1 += i**2
        num2 += i
    num2 = num2 ** 2
    return num2 - num1

print(sumSquareDif())