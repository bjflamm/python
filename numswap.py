# //swap numbers with no temp variable
# have to use the difference of the numbers
def numswap(num1,num2):
    num1 = num1 - num2
    num2 = num2 + num1
    num1 = num2 - num1
    return(num1,num2)

print(numswap(3, 10))