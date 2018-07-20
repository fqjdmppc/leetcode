# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        q = [(_.val, id(_), _) for _ in lists if _]
        if not q:
            return None
        heapq.heapify(q)
        head = heapq.heappop(q)[-1]
        if head.next:
            heapq.heappush(q, (head.next.val, id(head.next), head.next))
        head.next = None
        cur = head
        while q:
            cur.next = heapq.heappop(q)[-1]
            if cur.next.next:
                heapq.heappush(q, (cur.next.next.val, id(cur.next.next), cur.next.next))
            cur = cur.next
            cur.next = None
        
        return head
            
        
        