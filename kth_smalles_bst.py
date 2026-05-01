# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_array = []
        self.in_order(root, sorted_array)
        return sorted_array[k - 1]

    def in_order(self, current_node, sorted_array):
        if current_node == None:
            return 

        self.in_order(current_node.left, sorted_array)
        sorted_array.append(current_node.val)
        self.in_order(current_node.right, sorted_array)

        return
