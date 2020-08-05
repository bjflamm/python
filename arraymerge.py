# /merge two sorted arrays
def arraymerge(arr1, arr2):
    merged_array = []
    i = 1
    j = 1
    arr1elm = arr1[0]
    arr2elm = arr2[0]
    elms_remain = True

    while(elms_remain):
        if arr1elm < arr2elm and i < len(arr1):
            merged_array.append(arr1elm)
            arr1elm = arr1[i]
            i += 1
            
        elif j < len(arr2):
            merged_array.append(arr2elm)
            arr2elm = arr2[j]
            j += 1
        
        elif arr1elm == arr2elm:
            merged_array.append(arr1elm)
            merged_array.append(arr2elm)
            arr1elm = arr1[i]
            arr2elm = arr2[j]
            i += 1
            j += 1

        else:
            elms_remain = False
    return merged_array
    

print(arraymerge([1,2,3,4,4],[1,3,4,5,6,6]))