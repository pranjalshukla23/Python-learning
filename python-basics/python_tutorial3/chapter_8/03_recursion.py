def factorial(n):
    #base condition
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
result = factorial(10)

print(result)