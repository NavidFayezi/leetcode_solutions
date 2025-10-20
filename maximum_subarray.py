class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """Return the sum of maximum subarray in nums.

        For a given array, this function applies the Kadane's algorithm to
        obtain the sum of the maximum subarray in ``nums``.

        Args:
            nums (list[int]): A non-empty list of integers.

        Returns:
            int: The sum of the contiguous subarray with the largest sum.

        Raises:
            ValueError: If ``nums`` is empty.

        Notes:
            - Time complexity: O(n)
            - Space complexity: O(n) in this implementation because the
              current subarray is tracked as a list; this can be reduced to
              O(1) by tracking only sums instead of the subarray itself.
        """

        if not nums:
            raise ValueError("nums must be a non-empty list")

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

