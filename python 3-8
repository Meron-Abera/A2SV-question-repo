class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None:
            return 
        elif head.next==None:
            return head
        else:
            moving = head
            stable = head
            while moving.next!=None:
                if moving.next.val!=moving.val:
                    stable.next = moving.next
                    stable = moving.next
                moving = moving.next
            stable.next=None        
            return head
