class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n // 2):
            for j in range(i, n - i - 1):
                to_i_j = matrix[n - 1 - j][i]
                to_n1j_i = matrix[n - 1 - i][n - 1 - j]
                to_n1i_n1j = matrix[j][n - 1 - i]
                to_j_n1i = matrix[i][j]
                matrix[i][j] = to_i_j
                matrix[n - 1 - j][i] = to_n1j_i
                matrix[n - 1 - i][n - 1 - j] = to_n1i_n1j
                matrix[j][n - 1 - i] = to_j_n1i


