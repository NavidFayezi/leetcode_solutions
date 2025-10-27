class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """Convert `s` into its ZigZag form and return the resulting string.

        Args:
            s (str): The input string to convert.
            numRows (int): Number of rows to use for the ZigZag pattern.

        Returns:
            str: The converted string read row-by-row from the ZigZag pattern.

        Notes:
            This implementation builds a list of columns (each column is a
            list of length `numRows`) that form a transposed view of the
            ZigZag, then delegates to `zigzag_matrix_to_str` to flatten it.
        """
        zigzag_matrix = []  # transpose of the answer matrix
        index = 0
        str_length = len(s)

        column_counter = 0
        direction = 0
        while index < str_length:
            column_counter = column_counter % numRows
            
            # this prevents double full columns
            if column_counter == numRows - 1:
                column_counter = 0
            
            # this is the column you can fill completely
            if column_counter == 0:
                
                # the for loop fills a column
                temp = ["" for i in range(numRows)]
                for i in range(numRows):
                    if index >= str_length:
                        break
                    else:
                        temp[i] = s[index]
                        index += 1
                
                zigzag_matrix.append(temp)  # append the column to the matrix
                column_counter += 1
            
            # this is the column that should only contain one letter
            else:
                if direction == 0:
                    for i in range(numRows - 2, 0, -1):
                        if index >= str_length:
                            break
                        else:
                            temp = ["" for i in range(numRows)]
                            temp[i] = s[index]
                            zigzag_matrix.append(temp)
                            index += 1
                            column_counter = (column_counter + 1) % numRows
                            if column_counter == 0 or column_counter == numRows - 1:
                                break
                    
                else:
                    for i in range(1, numRows - 1):
                        if index >= str_length:
                            break
                        else:
                            temp = ["" for i in range(numRows)]
                            temp[i] = s[index]
                            zigzag_matrix.append(temp)
                            index += 1
                            column_counter = (column_counter + 1) % numRows
                            if column_counter == 0 or column_counter == numRows - 1:
                                break
        
        return self.zigzag_matrix_to_str(zigzag_matrix, numRows)
    

    def zigzag_matrix_to_str(self, zigzag: list, numrows: int) -> str:
        """Flatten a column-oriented zigzag matrix into a single string.

        Args:
            zigzag (list[list[str]]): List of columns where each column is a
                list of strings (one per row). Empty strings represent empty
                cells.
            numrows (int): Number of rows in the ZigZag pattern.

        Returns:
            str: The flattened string produced by reading the ZigZag row by
                row from top to bottom and left to right.
        """
        res = ""
        for i in range(numrows):
            for chars in zigzag:
                res = res + chars[i]
        
        return res


# I can tell this is not the most efficient solution, but the problem is silly
# so I won't try to optimize it (it's already O(n) time complexity anyway)
if __name__ == "__main__":
    test_input = "PAYPALISHIRING"
    solution = Solution()
    print(solution.convert(test_input, 3))