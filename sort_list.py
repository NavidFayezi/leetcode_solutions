class Solution:
    def sortList(self, head):
        if head == None or head.next == None:
            return head

        else:
            before_mid = None
            temp = head
            mid = head
            change_mid = True
            temp = temp.next
            while temp is not None:
                if change_mid is False:
                    change_mid = True
                else:
                    change_mid = False
                    before_mid = mid
                    mid = mid.next
                temp = temp.next

            before_mid.next = None
            sorted_list_1 = self.sortList(head)
            sorted_list_2 = self.sortList(mid)
            merged_head = self.merge_linked_lists(sorted_list_1, sorted_list_2)
            return merged_head
    
    def merge_linked_lists(self, head1, head2):
        merged_head = None
        if head1.val <= head2.val:
            merged_head = head1
            head1 = head1.next
        else:
            merged_head = head2
            head2 = head2.next
        
        temp = merged_head
        while True:
            if head1 is None:
                temp.next = head2
                break
            elif head2 is None:
                temp.next = head1
                break
            
            else:
                if head1.val <= head2.val:
                    temp.next = head1
                    head1 = head1.next
                    temp = temp.next
                else:
                    temp.next = head2
                    head2 = head2.next
                    temp = temp.next
        
        return merged_head
