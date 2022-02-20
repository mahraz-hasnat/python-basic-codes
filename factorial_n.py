# the factorial function return the factorial of n
def factorial(n):
    result = 1
    for x in range(1, n+1):
        result = x * result
    return result
 
for n in range(0,10):
