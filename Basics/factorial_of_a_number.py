num = int(input("enter a number: "))

factorial = 1

if num < 0:
    print("sorry, negative number does not have factorials")
elif num == 0:
    print("factorial of zero is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial + i
    print("the factorial of ", num, "is ", factorial)