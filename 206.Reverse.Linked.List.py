# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def go(p, ret):
            if p.next is None: 
                ret[0] = p
                return p
            else:
                go(p.next, ret).next = p
                return p
        
        if head is None: return None
        ret = [None]
        go(head, ret).next = None
        return ret[0]