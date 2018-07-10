# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = head
        nth = None
        counter = 0
        while head != None:
            head = head.next
            if counter < n: counter += 1
            else: nth = first if nth is None else nth.next
        if nth is None:
            return first.next
        else:
            nth.next = nth.next.next
            return first
