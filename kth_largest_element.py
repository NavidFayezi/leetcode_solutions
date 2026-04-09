class Max_Heap:
    def __init__(self, elements: list[int] = []):
        self.elements = elements
        self.heap_size = len(self.elements)
        lowest_index_leaf = self.heap_size // 2
        for i in range(lowest_index_leaf - 1, -1, -1):
             self.max_heapify(i)
    
    # These should be macros...
    def parent(self, index: int):
        return (index - 1) // 2

    def left_child(self, index: int):
        return (index * 2) + 1

    def right_child(self, index: int):
        return (index * 2) + 2

    def max_heapify(self, index: int):
        # this function assumes that the left and right child
        # satisfy the max heap property
        left_child = self.left_child(index)
        right_child = self.right_child(index)
        
        if left_child >= self.heap_size and \
           right_child >= self.heap_size:
             # reached a leaf node
             return

        temp_max = index
        if left_child < self.heap_size and \
            self.elements[left_child] > self.elements[temp_max]:
                temp_max = left_child

        if right_child < self.heap_size and \
            self.elements[right_child] > self.elements[temp_max]:
                temp_max = right_child

        if temp_max == index:
            # already satisfies heap property, so do nothing
            return
        
        else:
            temp = self.elements[temp_max]
            self.elements[temp_max] = self.elements[index]
            self.elements[index] = temp
            self.max_heapify(temp_max)
    
    def pop_max(self):
        assert(self.heap_size > 0)
        max_element = self.elements[0]
        self.elements[0] = self.elements[self.heap_size - 1]
        self.elements.pop()
        self.heap_size = len(self.elements)
        self.max_heapify(0)
        return max_element 

            

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap_1 = Max_Heap(nums)
        max_element = None
        for i in range(k):
            max_element = heap_1.pop_max()
        return max_element
