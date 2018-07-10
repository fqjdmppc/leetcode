// # Definition for singly-linked list.
// # class ListNode(object):
// #     def __init__(self, x):
// #         self.val = x
// #         self.next = None

// class Solution(object):
//     def getIntersectionNode(self, headA, headB):
//         """
//         :type head1, head1: ListNode
//         :rtype: ListNode
//         """
//         if not headA or not headB:
//             return None
//         p1, p2 = headA, headB
//         while p1 != p2:
//             p1 = p1.next if p1.next is not None else headA
//             p2 = p2.next if p2.next is not None else headB
//             if p1 == headA and p2 == headB:
//                 return None
//         return p1
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (headA == NULL || headB == NULL)
            return NULL;
        else
        {
            ListNode* p1 = headA, *p2 = headB;
            while (p1 != p2)
            {
                p1 = p1->next != NULL ? p1->next : headA;
                p2 = p2->next != NULL ? p2->next : headB;
                if (p1 == headA && p2 == headB)
                {
                    return NULL;
                }
            }
            return p1;
        }
    }
};