class Solution(object):
    
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        j = 0
        for val in A:
            val = val[::-1]
            i = 0
            for num in val:
                num = 1 - num
                val[i] = num
                i += 1
            A[j] = val
            j += 1
        
        return A