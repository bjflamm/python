# def num_list_gen(list):
#     numlist = []
#     for i in range(0, len(list)):
#         if list[i] == ' ' or list[i] == ',':
#             continue
#         else:
#             numlist.append(list[i])
#     return numlist;


def num_list_gen(list):
    numlist = []
    for i in range(0, len(list)):
        if list[i].isdigit():
            numlist.append(list[i])
            
            
    return numlist, tuple(numlist);
nums = raw_input("Enters nums like 1, 2, 3, 4, etc.: ")

print(num_list_gen(nums))