# /merge two sorted arrays
def arraymerge(arr1, arr2):
    merged_array = []
    i = 0
    j = 0

    if len(arr1) > 0:
        arr1elms_exist = True;
        elms_remain = True;
    else:
        arr1elms_exist = False; 

    if len(arr2) > 0:
        arr2elms_exist = True;
        elms_remain = True;
    else:
        arr2elms_exist = False;

    while(elms_remain):
        
        if i == len(arr1):
            arr1elms_exist = False;

        if j == len(arr2):
            arr2elms_exist = False;

        if arr1elms_exist and arr2elms_exist:
            arr1elm = arr1[i]
            arr2elm = arr2[j]
            if arr1elm < arr2elm:
                merged_array.append(arr1elm)
                
                i += 1

            elif arr2elm < arr1elm:
                merged_array.append(arr2elm)
                
                j += 1

            elif arr1elm == arr2elm:
                merged_array.append(arr1elm)
                merged_array.append(arr2elm)

                i += 1
                j += 1
        
        elif arr1elms_exist and not arr2elms_exist:
            arr1elm = arr1[i]
            merged_array.append(arr1elm);
  
            i += 1

        elif arr2elms_exist and not arr1elms_exist:
            arr2elm = arr2[j]
            merged_array.append(arr2elm);
            j += 1

        else:
            elms_remain = False
    return merged_array
    

print(arraymerge([1,3,4,5,6,6],[1,2,3,4,4]))
print(arraymerge([1,2,3,4,4],[1,3,4,5,6,6]))
print(arraymerge([], [1,2,3,3,4]))
print(arraymerge([1,3,4,5,6,6,7], []))
print(arraymerge([1,1,1,1,1], [1,1,1,1,1]))