import math


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, -math.inf, math.inf)

    def validate(self, node, sub_tree_min, sub_tree_max):
        if node is None:
            return True

        res = True
        if (
            (node.val >= sub_tree_max or node.val <= sub_tree_min)
            or (node.left is not None and node.left.val >= node.val)
            or (node.right is not None and node.right.val <= node.val)
        ):
            res = False

        right_res = self.validate(node.right, node.val, sub_tree_max)
        left_res = self.validate(node.left, sub_tree_min, node.val)
        res = res and right_res and left_res

        return res
