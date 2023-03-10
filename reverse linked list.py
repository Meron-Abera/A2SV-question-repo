class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev
