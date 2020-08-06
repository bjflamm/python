#this is a leetcode problem with the goal of adding 2 linked lists i.e. (2->4 + 5->6 = 7->0->1) 42+65 = 107
# won't work when the addition of the first digit results in a remainder

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        curr_node_l1 = l1
        curr_node_l2 = l2
        
        nodes_remain = True
        carry = 0
        
        return_val = 0
        
        while(nodes_remain):
            
            
            if curr_node_l1 != None and curr_node_l2 != None:
                if carry == 1:
                    li_sum = curr_node_l1.val + curr_node_l2.val + carry
                    carry = 0
                else:
                    li_sum = curr_node_l1.val + curr_node_l2.val

                if li_sum % 10 < li_sum:
                    carry += 1
                    curr_node_l1.val = li_sum % 10
                    curr_node_l2.val = li_sum % 10
                else:
                    curr_node_l1.val = li_sum
                    curr_node_l2.val = li_sum

                curr_node_l1 = curr_node_l1.next
                curr_node_l2 = curr_node_l2.next
                
                
            elif curr_node_l1 == None and curr_node_l2 != None:
                
                return_val = 1
                if carry == 1:
                    li_sum = curr_node_l2.val + carry
                    carry = 0
                else:
                    li_sum = curr_node_l2.val

                if li_sum % 10 < li_sum:
                    carry += 1
                    curr_node_l2.val = li_sum % 10
                else:
                    curr_node_l2.val = li_sum

                curr_node_l2 = curr_node_l2.next
                
                
                    
            elif curr_node_l2 == None and curr_node_l1 != None:
                
                if carry == 1:
                    li_sum = curr_node_l1.val + carry
                    carry = 0
                else:
                    li_sum = curr_node_l1.val

                if li_sum % 10 < li_sum:
                    carry += 1
                    curr_node_l1.val = li_sum % 10
                else:
                    curr_node_l1.val = li_sum

                curr_node_l1 = curr_node_l1.next
                
                
                
            else:
                nodes_remain = False
                
            
        if return_val == 0:
            return l1
        else:
            return l2
        