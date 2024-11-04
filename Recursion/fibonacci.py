# def Fibonacci(n):
#     if(n<=1):
#         return n
#     return Fibonacci(n-1)+Fibonacci(n-2)

# number=int(input("Enter the number: "))
# print(Fibonacci(number))
# for i in range(number):
#     print(Fibonacci(i))




def fibonacci(n, memo={}):
    # Base cases
    if n <= 1:
        return n
    
    # Check if the value is already calculated
    if n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    
    return memo[n]

# Test the function
n = 8
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
