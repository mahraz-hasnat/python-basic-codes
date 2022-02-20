# the factorial function return the factorial of n and after the function the loop prints the factorials from 0 to 9
def factorial(n):
    result = 1
    for x in range(1, n+1):
        result = x * result
    return result
 
for n in range(0,10):
    print(n, factorial(n)
