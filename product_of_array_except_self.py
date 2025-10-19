"""Utilities for computing the product of array elements except self.

This module provides a Solution class with a method to compute the product
of all elements of a list except the element at each index, without using
division and in O(n) time with O(n) additional space.

Example:
    >>> Solution().productExceptSelf([1, 2, 3, 4])
    [24, 12, 8, 6]

The implementation constructs prefix (left) and suffix (right) product
lists and multiplies corresponding entries to produce the result.
"""


class Solution:
    """Encapsulates solutions to LeetCode algorithmic problems.

    Provides methods to compute results for various problems efficiently.
    """

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """Return a list where each element is the product of all other elements.

        Computes, for each index i in ``nums``, the product of all elements of
        ``nums`` except ``nums[i]``. Division is not used. The algorithm runs
        in O(n) time and uses O(n) extra space for the prefix and suffix
        product lists.

        Args:
            nums: A list of integers. It may contain zeros. The function does
                not modify the input list.

        Returns:
            A list of integers of the same length as ``nums`` where the value
            at index i is the product of all elements in ``nums`` except
            ``nums[i]``.

        Raises:
            ValueError: If ``nums`` is empty. (This behavior mirrors typical
                LeetCode constraints where an empty input is not expected but
                is explicitly rejected here for clarity.)

        Examples:
            >>> Solution().productExceptSelf([1, 2, 3, 4])
            [24, 12, 8, 6]
        """

        if not nums:
            raise ValueError("nums must be a non-empty list")

        left_product = [1]

        # right_product should be reversed at the end of the loop
        right_product = [1]
        list_length = len(nums)

        for i in range(1, list_length):
            left_product.append(left_product[-1] * nums[i - 1])
            right_product.append(right_product[-1] * nums[list_length - i])

        right_product = right_product[::-1]

        # a list whose ith element is the product of all elements in nums
        # except for nums[i]
        answer = []
        for i in range(list_length):
            answer.append(left_product[i] * right_product[i])

        return answer


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4]
    print(solution.productExceptSelf(nums))  # Output: [24, 12, 8, 6]
