class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [[0 for i in range(9)] for i in range(9)]
        columns = [[0 for i in range(9)] for i in range(9)]
        boxes = [[0 for i in range(9)] for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    pass
                else:
                    value = int(board[i][j]) - 1
                    box_number = (i // 3) * 3 + (j // 3)

                    boxes[box_number][value] += 1
                    columns[j][value] += 1
                    rows[i][value] += 1

                    if (
                        boxes[box_number][value] > 1
                        or columns[j][value] > 1
                        or rows[i][value] > 1
                    ):
                        return False
        
        return True
