class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board) - 1
        cols = len(board[0]) - 1

        to_be_updated = []
        for i in range(rows + 1):
            for j in range(cols + 1):
                current_cell = board[i][j]
                live_neighbours = 0
                neighbours = self.neighbours(i, j, cols, rows)
                for pair in neighbours:
                    live_neighbours += board[pair[0]][pair[1]]

                if self.lives(current_cell, live_neighbours) ^ board[i][j] == 1:
                    to_be_updated.append((i, j))

        for pair in to_be_updated:
            board[pair[0]][pair[1]] ^= 1

    def lives(self, state, live_neighbours):
        rc = 0
        if state == 1:
            if live_neighbours < 2 or live_neighbours > 3:
                rc = 0
            else:
                rc = 1
        else:
            if live_neighbours == 3:
                rc = 1
            else:
                rc = 0

        return rc

    def neighbours(self, i, j, cols, rows):
        res = []
        offsets = [-1, 0, 1]
        for r in offsets:
            for c in offsets:
                neighbour_i = i + r
                neighbour_j = j + c
                if (
                    neighbour_i > rows
                    or neighbour_i < 0
                    or neighbour_j > cols
                    or neighbour_j < 0
                    or (neighbour_i == i and neighbour_j == j)
                ):
                    continue

                res.append((neighbour_i, neighbour_j))

        return res
