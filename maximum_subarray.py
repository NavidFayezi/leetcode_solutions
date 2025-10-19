class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        # I am also keeping track of the actual subarray here.
        # The first element of tuple is the actual sum,
        # and the second element is the elements that sum to the first element
        max_sum = (nums[0], [nums[0]])
        current_sum = (max_sum[0], max_sum[1])
        array_length = len(nums)

        for i in range(1, array_length):
            if current_sum[0] < 0:
                current_sum = (nums[i], [nums[i]])
            else:
                current_sum = (
                    current_sum[0] + nums[i],
                    current_sum[1] + [nums[i]],
                )
            if current_sum[0] >= max_sum[0]:
                max_sum = (current_sum[0], current_sum[1])

        return max_sum[0]


if __name__ == "__main__":
    solution = Solution()
    test_input = [2, 3, -8, 7, -1, 2, 3]  # Output: 11
    print(solution.maxSubArray(test_input))
