import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        sorted_array = []
        self.in_order(root, sorted_array)
        
        min_diff = math.inf
        array_len = len(sorted_array)
        for i in range(1, array_len):
            temp = abs(sorted_array[i] - sorted_array[i - 1])
            if temp < min_diff:
                min_diff = temp

        return min_diff

    def in_order(self, current_node, sorted_array):
        if current_node == None:
            return 

        self.in_order(current_node.left, sorted_array)
        sorted_array.append(current_node.val)
        self.in_order(current_node.right, sorted_array)

        return
