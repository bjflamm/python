def ordered_search(olist, value):
    if len(olist) == 0:
        return False
    else:
        midpoint = len(olist)/2
        
    if olist[midpoint] == value:
        return True
    else:
        if value < olist[midpoint]:
            out = binarysearch(olist[:midpoint], value)
            return out
        else:
            out = binarysearch(olist[midpoint+1:], value)
            return out

def binarysearch(olist, value):
    first = 0
    found = False
    last = len(olist)-1
    while(first <= last and not found):
        midpoint = (first + last) /2
        if value == midpoint:
            found = True
        else:
            if value < midpoint:
                first = 0
                last = midpoint - 1
            else:
                first = midpoint + 1
                
    return found

print(ordered_search([0, 1, 3, 8, 14, 18, 19, 34, 52], 17))