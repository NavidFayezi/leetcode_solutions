# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """Calls a helper function that traverses the tree and appends the
           node on the right side to a list.

        Args:
            root (Optional[TreeNode]): the root of the tree.

        Returns:
            List[int]: the list of nodes from right side's pov.
        """
        if root == None:
            return []
        else:
            self.rs_list = [root.val]
            self.custom_traversal(root, 2)
            return self.rs_list

    def custom_traversal(self, tn: Optional[TreeNode], depth: int):
        """Traverses the tree and appends the node on the right side to a list.

        Args:
            tn (Optional[TreeNode]): a tree node.
            depth (int): determines the depth of tn's immediate children.

        Returns:
            None
        """
        if tn == None:
            return

        if len(self.rs_list) < depth:
            if tn.right != None:
                self.rs_list.append(tn.right.val)
            elif tn.left != None:
                self.rs_list.append(tn.left.val)

        self.custom_traversal(tn.right, depth + 1)
        self.custom_traversal(tn.left, depth + 1)
