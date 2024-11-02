def Fibonacci(n):
    if(n<=1):
        return n
    return Fibonacci(n-1)+Fibonacci(n-2)

number=int(input("Enter the number: "))
print(Fibonacci(number))
for i in range(number):
    print(Fibonacci(i))