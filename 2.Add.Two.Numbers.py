# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = 0
        aa = 1
        while l1 is not None:
            a += l1.val * aa
            aa *= 10
            l1 = l1.next
        b = 0
        aa = 1
        while l2 is not None:
            b += l2.val * aa
            aa *= 10
            l2 = l2.next
            
        a += b
        cur = head = ListNode(a % 10)
        a //= 10
        while a:
            cur.next = ListNode(a % 10)
            cur = cur.next
            a //= 10
            
        return head
            
            