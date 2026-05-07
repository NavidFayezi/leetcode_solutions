# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        temp = res
        carry = 0
        while True:
            if l1 is not None or l2 is not None:
                temp.next = ListNode()
                temp = temp.next
                d1 = 0
                d2 = 0

                if l1 is not None:
                    d1 = l1.val

                if l2 is not None:
                    d2 = l2.val
            
                temp.val = (d1 + d2 + carry) % 10
                carry = (d1 + d2 + carry) // 10
            
                if l1 is not None:
                    l1 = l1.next
                if l2 is not None:
                    l2 = l2.next

            else:
                if carry > 0:
                    temp.next = ListNode(val = carry)
                break
        
        return res.next
