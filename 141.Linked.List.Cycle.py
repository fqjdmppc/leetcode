# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None: return False
        while not (head.next == None or head.next == head):
            n = head.next
            head.next = head
            head = n
            
        return True if head.next == head else False