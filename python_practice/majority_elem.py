class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        curr_mode = nums[0]
        
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1
                
            if num_dict[num] > num_dict[curr_mode]:
                curr_mode = num
                
        return curr_mode

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_list = {}
        num_array = []
        length = len(nums)
        
        for num in nums:
            if num not in num_list:
                num_list[num] = 1
            else:
                num_list[num] += 1
            if num_list[num] > (length/3) and num not in num_array:
                num_array.append(num)
                
        return num_array
        