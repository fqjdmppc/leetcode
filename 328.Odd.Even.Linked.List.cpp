/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* oddEvenList(struct ListNode* head) {
    if (head == NULL || head->next == NULL) return head;
    struct ListNode* odd = head,*even = head->next,*odd_first = head,*even_first = head->next;
    head=head->next->next;
    int count = 0;
    while (head!=NULL)
    {
        if (!count)
        {
            odd->next = head;
            odd = odd->next;
        }
        else
        {
            even->next = head;
            even = even->next;
            
        }
        head = head->next;
        count ^= 1;
    }
    odd->next = even_first;
    even->next = NULL;
    return odd_first;
}