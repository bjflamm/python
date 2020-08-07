def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def fib_norec(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
    
        


print(fib_norec(6))