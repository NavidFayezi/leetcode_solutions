import collections
import numpy


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = numpy.zeros((m, n), dtype=bool)

        no_islands = 0
        bfs_queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and seen[i][j] == False:
                        no_islands += 1
                        bfs_queue.append((i, j))
                        while len(bfs_queue) > 0:
                            queue_size = len(bfs_queue)
                            for _ in range(queue_size):
                                indices = bfs_queue.popleft()
                                if (
                                    grid[indices[0]][indices[1]] == "1"
                                    and seen[indices[0]][indices[1]] == False
                                ):
                                    seen[indices[0]][indices[1]] = True
                                    if (
                                        indices[1] + 1 < n
                                        and seen[indices[0]][indices[1] + 1]
                                        == False
                                    ):
                                        bfs_queue.append(
                                            (indices[0], indices[1] + 1)
                                        )
                                    if (
                                        indices[0] + 1 < m
                                        and seen[indices[0] + 1][indices[1]] 
                                        == False
                                    ):
                                        bfs_queue.append(
                                            (indices[0] + 1, indices[1])
                                        )
                                    if (
                                        indices[1] - 1 >= 0
                                        and seen[indices[0]][indices[1] - 1]
                                        == False
                                    ):
                                        bfs_queue.append(
                                            (indices[0], indices[1] - 1)
                                        )
                                    
                                    if (
                                        indices[0] - 1 >= 0
                                        and seen[indices[0] - 1][indices[1]]
                                        == False
                                    ):
                                        bfs_queue.append(
                                            (indices[0] - 1, indices[1])
                                        )
        return no_islands
