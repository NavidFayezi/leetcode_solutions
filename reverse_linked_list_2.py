# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        new_head = head
        counter = 1
        last_unchanged = None
        while counter < left:
            counter += 1
            last_unchanged = head
            head = head.next
        
        cut_off_head = head

        next_reversed = None
        while counter <= right:
            counter += 1
            temp = head.next
            head.next = next_reversed
            next_reversed = head
            head = temp
            if head is None:
                break
        
        cut_off_head.next = head
        if left > 1:
            last_unchanged.next = next_reversed
        else:
            new_head = next_reversed
        
        return new_head
