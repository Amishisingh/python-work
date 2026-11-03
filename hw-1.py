number1 = int(input("Enter your number: "))
number2 = int(input("Enter your number2: "))



for i in range(2, number1 + 1):
    if number1 % i == 0 and number2 % i == 0:
        print(i)