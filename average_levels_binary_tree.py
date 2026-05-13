# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        
        else:
            queue = collections.deque([root])
            res = []

            while len(queue) > 0:
                current_level_nodes = len(queue)
                current_level_sum = 0

                for _ in range(current_level_nodes):
                    node = queue.popleft()
                    current_level_sum += node.val
                    
                    if node.right is not None:
                        queue.append(node.right)
                    
                    if node.left is not None:
                        queue.append(node.left)
                
                res.append(current_level_sum / current_level_nodes)
            
            return res
