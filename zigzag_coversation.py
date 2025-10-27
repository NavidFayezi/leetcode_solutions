class Solution:
    def convert(self, s: str, numRows: int) -> str:
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
        res = ""
        for i in range(numrows):
            for chars in zigzag:
                res = res + chars[i]
        
        return res


if __name__ == "__main__":
    test_input = "PAYPALISHIRING"
    solution = Solution()
    print(solution.convert(test_input, 3))