# //calculate gcd of two numbers

def gcd(num1,num2):
    divisor = 1
    gcd = 1
    while(divisor <= num1 and divisor <= num2):
        if(num1 % divisor == 0) and (num2 % divisor == 0):
            gcd = divisor
        divisor += 1
    return gcd

def gcd2(num1,num2):
    gcd = 1
    if(num1 < num2):
        for i in range(1,num1-1):
            if(num1 % i == 0 and num2 % i == 0):
                gcd = i
    else:
        for i in range(1,num2-1):
            if(num1 % i == 0 and num2 % i == 0):
                gcd = i
                
    return gcd
print(gcd2(40,30))