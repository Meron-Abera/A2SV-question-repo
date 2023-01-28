# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c = 0
        x = ListNode(-1)
        h = x
        while l1 or l2 or c:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            if l1:l1 = l1.next
            if l2:l2 = l2.next
            s = n1+n2+c
            c = s//10
            x.next = ListNode(s%10)
            x = x.next
        return h.next
