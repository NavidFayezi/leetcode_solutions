class Solution:
    dir = [0, 1, 2, 3]

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m = len(matrix)
        n = len(matrix[0])
        no_elements = m * n

        counter = 0
        indices = (0, 0)
        direction = Solution.dir[0]
        res = []
        up = 0
        down = m - 1
        left = 0
        right = n - 1
        while counter < no_elements:
            res.append(matrix[indices[0]][indices[1]])
            counter += 1
            if direction == Solution.dir[0]:
                if indices[1] < right:
                    indices = (indices[0], indices[1] + 1)  # keep going right
                else:
                    indices = (indices[0] + 1, indices[1])  # go down
                    up += 1
                    direction = (Solution.dir[direction] + 1) % 4

            elif direction == Solution.dir[1]:
                if indices[0] < down:
                    indices = (indices[0] + 1, indices[1])  # keep going down
                else:
                    indices = (indices[0], indices[1] - 1)  # go left
                    right -= 1
                    direction = (Solution.dir[direction] + 1) % 4

            elif direction == Solution.dir[2]:
                if indices[1] > left:
                    indices = (indices[0], indices[1] - 1)  # keep going left
                else:
                    indices = (indices[0] - 1, indices[1])  # go up
                    down -= 1
                    direction = (Solution.dir[direction] + 1) % 4

            elif direction == Solution.dir[3]:
                if indices[0] > up:
                    indices = (indices[0] - 1, indices[1])  # keep going up
                else:
                    indices = (indices[0], indices[1] + 1)  # go right
                    left += 1
                    direction = (Solution.dir[direction] + 1) % 4

            else:
                print("ERROR")
                break

        return res
