class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new_array = []
        num1_index = 0
        num2_index = 0
        
        length1 = len(nums1)
        length2 = len(nums2)
        
        new_array_len = length1 + length2
        elems_remain = True
        
        while(elems_remain):
            if num1_index < length1 and num2_index < length2:
                if nums1[num1_index] < nums2[num2_index]:
                    new_array.append(nums1[num1_index])
                    num1_index += 1
                else:
                    new_array.append(nums2[num2_index])
                    num2_index += 1
                    
            elif num1_index < length1 and num2_index == length2:
                new_array.append(nums1[num1_index])
                num1_index += 1
                
            elif num2_index < length2 and num1_index == length1:
                new_array.append(nums2[num2_index])
                num2_index += 1
            else:
                    elems_remain = False

        #check for median
        if new_array_len % 2 != 0 and new_array_len > 2:
            median = float(new_array[new_array_len/2])
            
        elif new_array_len % 2 == 0 and new_array_len == 2:
            median = float(new_array[0] + new_array[1])/2
            
        else:
            median = float(new_array[(new_array_len/2)-1] + new_array[(new_array_len/2)])/2
            
        return median
                