import collections
import numpy


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        seen = numpy.zeros((m, n), dtype=bool)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and seen[i][j] == False:
                    queue = collections.deque([(i, j)])
                    capture = True
                    capture_list = []

                    while len(queue) > 0:
                        current_size = len(queue)

                        for _ in range(current_size):
                            cell = queue.popleft()
                            if seen[cell[0]][cell[1]] == False:
                                capture_list.append(cell)
                                seen[cell[0]][cell[1]] = True

                                if (
                                    cell[0] == 0
                                    or cell[0] == m-1
                                    or cell[1] == 0
                                    or cell[1] == n-1
                                ):
                                    capture = False
                                
                                if (
                                    cell[0] - 1 >= 0
                                    and board[cell[0] - 1][cell[1]] == "O"
                                    and seen[cell[0] - 1][cell[1]] == False
                                ):
                                    queue.append((cell[0] - 1, cell[1]))
                                
                                if (
                                    cell[0] + 1 < m
                                    and board[cell[0] + 1][cell[1]] == "O"
                                    and seen[cell[0] + 1][cell[1]] == False
                                ):
                                    queue.append((cell[0] + 1, cell[1]))
                                
                                if (
                                    cell[1] - 1 >= 0
                                    and board[cell[0]][cell[1] - 1] == "O"
                                    and seen[cell[0]][cell[1] - 1] == False
                                ):
                                    queue.append((cell[0], cell[1] - 1))
                                
                                if (
                                    cell[1] + 1 < n
                                    and board[cell[0]][cell[1] + 1] == "O"
                                    and seen[cell[0]][cell[1] + 1] == False
                                ):
                                    queue.append((cell[0], cell[1] + 1))
                            
                    if capture == True:
                        for cell in capture_list:
                            board[cell[0]][cell[1]] = "X"
