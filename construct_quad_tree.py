"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: list[list[int]]) -> "Node":

        return self.make_tree(grid, 0, 0, len(grid))

    def make_tree(self, grid: list[list[int]], start_i, start_j, rows):
        if rows == 1:
            new_node = Node(
                grid[start_i][start_j], True, None, None, None, None
            )
            return new_node

        else:
            first = grid[start_i][start_j]
            is_leaf = True
            for i in range(start_i, start_i + rows):
                for j in range(start_j, start_j + rows):
                    if grid[i][j] != first:
                        is_leaf = False
                        break

                if is_leaf == False:
                    break

            new_node = None
            if is_leaf == False:
                sub_grid_rows = rows // 2
                top_left_start = (start_i, start_j)
                top_right_start = (start_i, start_j + sub_grid_rows)
                bottom_left_start = (start_i + sub_grid_rows, start_j)
                bottom_right_start = (
                    start_i + sub_grid_rows,
                    start_j + sub_grid_rows,
                )
                top_left_node = self.make_tree(
                    grid, top_left_start[0], top_left_start[1], sub_grid_rows
                )
                top_right_node = self.make_tree(
                    grid, top_right_start[0], top_right_start[1], sub_grid_rows
                )
                bottom_left_node = self.make_tree(
                    grid,
                    bottom_left_start[0],
                    bottom_left_start[1],
                    sub_grid_rows,
                )
                bottom_right_node = self.make_tree(
                    grid,
                    bottom_right_start[0],
                    bottom_right_start[1],
                    sub_grid_rows,
                )
                new_node = Node(
                    1,
                    is_leaf,
                    top_left_node,
                    top_right_node,
                    bottom_left_node,
                    bottom_right_node,
                )
            else:
                new_node = Node(first, is_leaf, None, None, None, None)

            return new_node
