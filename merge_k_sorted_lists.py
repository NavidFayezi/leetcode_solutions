# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if lists == []:
            return None
        
        else:
            res = ListNode()
            res_end = res
            incomplete = True
            while incomplete == True:
                incomplete = False
                temp_min = ListNode(10**5)
                no_lists = len(lists)
                min_index = -1
                for i in range(no_lists):
                    if lists[i] is not None:
                        incomplete = True
                        if lists[i].val <= temp_min.val:
                            temp_min = lists[i]
                            min_index = i
                
                if incomplete == True:
                    lists[min_index] = lists[min_index].next
                    res_end.next = temp_min
                    res_end = res_end.next
            
            return res.next  
