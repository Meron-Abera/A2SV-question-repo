# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        retHead = ListNode()
        pre = retHead
        p = head
        stack = []
        while(p != None):
            if stack and p.val != stack[-1].val:
                if len(stack) > 1:
                    stack = []
                else:
                    pre.next = stack.pop()
                    pre = pre.next
            stack.append(p)
            p = p.next
        if len(stack) > 1:
            pre.next = None
        if len(stack) == 1:
            pre.next = stack.pop()
        return retHead.next
