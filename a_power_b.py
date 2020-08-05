# //compute num a ^ b
def a_power_b(a,b):
    out = 1;
    ind = b;
    while(ind>0):
        out = out*a
        ind = ind - 1
    return

def a2(a,b):
    num1 = a
    for i in range(0,b-1):
        num1 = num1 * num1
    return num1

def power(a,b):
    num = 1;
    while b>0:
        num = num * a;
        b = b - 1;
    return num;

print(power(2,3))