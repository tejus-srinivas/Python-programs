a = int(input("enter first number = "))
b = int(input("enter second number = "))
sum = a + b
print("sum of first and second number = ",sum)
difference = a - b
if difference < 0 :
    print("difference is negative")
elif difference > 0 :
    print("difference is positive")
else :
    print("difference is zero")
print("\ndifference of first and second number = ",difference)
product = a * b
print("product of first and second number = ",product)
quotient = a // b
print("quotient of first and second number = ",quotient)
quit()
