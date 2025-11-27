class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_height = 0
        while left < right:
            area_of_water = (right - left) * min(height[left], height[right])
            if max_height < area_of_water:
                max_height = area_of_water
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                right -= 1

        return max_height


if __name__ == "__main__":
	solution = Solution()
	test_input = [1,8,6,2,5,4,8,3,7]
	print(Solution.maxArea(test_input))
