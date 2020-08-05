# bubble sort loops across array where #loops = range(list)
# i.e. given [1,4,3,2,5] the output of the first loop will be [1,3,2,4,5]
# second loop will be [1,2,3,4,5]
def bubble_sort(numlist):
    for i in range(len(numlist)-1,0,-1):
        for j in range(i):
            if numlist[j] > numlist[j+1]:
                temp = numlist[j]
                numlist[j] = numlist[j+1]
                numlist[j+1] = temp
    return numlist




def bubble_sort2(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

print(bubble_sort2([1, 4, 3, 2, 5]))