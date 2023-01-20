# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        f=head
        s=head
        while 1:
            if f.next==None:
                return s
            elif f.next.next==None:
                return s.next
            f=f.next.next
            s=s.next
