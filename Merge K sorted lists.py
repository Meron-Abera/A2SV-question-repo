# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappop,heappush,heapify
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []
        
        for l in lists:
            while l:
                heappush(h,l.val)
                l = l.next
        
        head = ListNode(0)
        head1 = head
        
        while h:
            head.next = ListNode(heappop(h))
            head = head.next
        
        return head1.next
