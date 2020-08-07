# find first character that doesn't repeat in a string
# select static index and compare to each index in the string
# if search_char == curr_char then continue, else return char
def firstnonrepeat(str1):

    for i in str1:
        charcount = 0
        for j in str1:
            if i == j:
                charcount+=1
        if charcount == 1:
            return i

def withdict(str1):

    exists = {}

    for char in str1:
        if char not in exists:
            exists[char] = 1

        else:
            exists[char] = exists[char] + 1
    
    for char in str1:
        if exists[char] == 1:
            return char

        
        

                
        

        
        



print(withdict("abdnejdjqdjjaskbjlksnlewwxx11z"))