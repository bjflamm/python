def factorial(n):
    if(n == 0):
        return 0
    elif(n==1):
        return 1
    else:
        return n * factorial(n-1)

def factorial_norec(n):
    out = 1
    for i in range(1,n+1):
        out = out * i
    return out

fact = {}
def factorial_hash(n):
    
    out = 1
    for i in range(1,n+1):
        if i in fact:
            print(True)
            out = out * fact[i]
        else:
            fact[i] = i * out
            out = out * i
    print(fact)
    return out,fact

print(factorial(6))
print(factorial_norec(6))
print(factorial_hash(6))
print(factorial_hash(7))