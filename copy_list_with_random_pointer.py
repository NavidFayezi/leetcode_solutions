# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None
        mapping = {}
        new_list = Node(head.val)
        rv = new_list
        mapping[head] = new_list

        while head.next is not None:
            if head.random is not None:
                if head.random in mapping:
                    new_list.random = mapping[head.random]
                else:
                    new_random = Node(head.random.val)
                    mapping[head.random] = new_random
                    new_list.random = new_random

            if head.next in mapping:
                new_list.next = mapping[head.next]
            else:
                new_node = Node(head.next.val)
                mapping[head.next] = new_node
                new_list.next = new_node
                
            head = head.next
            new_list = new_list.next
        
        if head.random is not None:
            if head.random in mapping:
                new_list.random = mapping[head.random]
        
        return rv
