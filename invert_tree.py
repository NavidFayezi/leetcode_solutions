# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Inverts a tree and returns its root.

        Args:
            root (Optional[TreeNode]): A TreeNode object, pointing to the
                                        root of the tree.
        Returns:
            Optional[TreeNode]: The root of the inverted tree.

        """
        if root == None:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
