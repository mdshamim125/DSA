def Factorial(n):
    if(n==0):
        return 1
    return n*Factorial(n-1)

number=int(input("enter the number: "))
print(Factorial(number))