class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        beginning = 0
        end = (m * n) - 1

        while end - beginning > 1:
            middle = (beginning + end) // 2
            temp = matrix[middle // n][middle % n]
            if temp == target:
                return True
            elif temp < target:
                beginning = middle
            else:
                end = middle
        
        if (
            matrix[end // n][end % n] == target
            or matrix[beginning // n][beginning % n] == target
        ):
            return True
        return False
