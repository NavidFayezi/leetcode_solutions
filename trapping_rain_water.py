class Solution:
    def trap(self, height: list[int]) -> int:
        """Compute how much water can be trapped.

        Args:
            height (list[int]): List of non-negative integers where each
                element represents the elevation of a bar and the width
                of each bar is 1.

        Returns:
            int: Total units of water that can be trapped.

        Example:
            >>> Solution().trap([4, 2, 0, 3, 2, 5])
            9

        Notes:
            Time complexity: O(n)
            Space complexity: O(n) due to the left_maxes list.
        """
        array_length = len(height)
        
        # This loop finds the left max of each element
        left_maxes =  [height[0]]
        for i in range(array_length - 1):
            if height[i] > left_maxes[-1]:
                left_maxes.append(height[i])
            else:
                left_maxes.append(left_maxes[-1])
        
        index = array_length - 1
        right_max = height[index]
        rain = 0
        while index >= 0:
            temp = min(right_max, left_maxes[index]) - height[index] 
            if temp > 0:
                rain += temp
            if height[index] > right_max:
                right_max = height[index]
            index -= 1
        return rain
        
        

if __name__ == "__main__":
    test_input = [4,2,0,3,2,5]
    solution = Solution()
    print(solution.trap(test_input))