# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import random
class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#         def plist(head):
#             while head:
#                 print(head.val, '->', end='')
#                 head = head.next
#             print('')
            
        def mysort(head): # ret: (head, tail)
            if not head or head.next is None:
                return (head, head)
            x = head
            for _ in range(random.randint(1, 777)):
                if x and x.next:
                    x = x.next
                else:
                    x = head
                    break
            x = x.val
            h = [ListNode(0), ListNode(0)]
            t = [h[0], h[1]]
            while head:
                if head.val < x:
                    t[0].next = head
                    head = head.next
                    t[0] = t[0].next
                    t[0].next = None
                    
                elif head.val > x:
                    t[1].next = head
                    head = head.next
                    t[1] = t[1].next
                    t[1].next = None
                else:
                    q = random.randint(0, 1)
                    t[q].next = head
                    head = head.next
                    t[q] = t[q].next
                    t[q].next = None
            # print("test", x)
            # plist(h[0])
            # plist(h[1])
            if h[0].next and not h[1].next:
                return mysort(h[0].next)
            elif not h[0].next and h[1].next:
                return mysort(h[1].next)
            else:
                ret = [mysort(h[0].next), mysort(h[1].next)]
                ret[0][1].next = ret[1][0]
                return (ret[0][0], ret[1][1])
            
        return mysort(head)[0]
                    