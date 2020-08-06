#leetcode problem to multiply 2 numbers (str type) and return the product as a string without using int()
class Solution(object):
    
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num_dict = {
            "0":0,
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9
        }
        num1_length = len(num1)-1
        num1_integer = 0
        
        for val in num1:
            multiplier = 10**num1_length
            curr_digit = num_dict[val]
            curr_digit = curr_digit * multiplier
            num1_integer += curr_digit
            num1_length -= 1
            
        num2_length = len(num2)-1
        num2_integer = 0
        
        for val in num2:
            multiplier2 = 10**num2_length
            curr_digit = num_dict[val]
            curr_digit = curr_digit * multiplier2
            num2_integer += curr_digit
            num2_length -= 1
        print(num1_integer,num2_integer)
        return str(num1_integer * num2_integer)
            
            