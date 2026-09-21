# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if lists == []:
            return None

        if len(lists) == 1:
            return lists[0]

        else:
            middle = len(lists) // 2
            list1 = self.mergeKLists(lists[:middle])
            list2 = self.mergeKLists(lists[middle:])
            my_lists = [list1, list2]
            res = ListNode()
            res_end = res
            incomplete = True
            min_node = ListNode(10**5)
            while incomplete == True:
                incomplete = False
                temp_min = min_node
                min_index = -1
                for i in range(2):
                    if my_lists[i] is not None:
                        incomplete = True
                        if my_lists[i].val <= temp_min.val:
                            temp_min = my_lists[i]
                            min_index = i
                
                if incomplete == True:
                    my_lists[min_index] = my_lists[min_index].next
                    res_end.next = temp_min
                    res_end = res_end.next
            
            return res.next
