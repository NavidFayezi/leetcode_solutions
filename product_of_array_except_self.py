class Solution:
    """Container for LeetCode problem solutions.

    This class groups small solution methods for common LeetCode problems.
    Methods are implemented for clarity and educational purposes rather than
    as production-grade library APIs.
    """

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """Return element-wise products of the input list excluding the element at each index.

        For each index i, compute the product of all elements of ``nums``
        except ``nums[i]``. The implementation avoids division by computing
        prefix and suffix products.

        Args:
            nums (list[int]): Input list of integers. May contain zeros.

        Returns:
            list[int]: A list where the value at index ``i`` is the product of
                all elements in ``nums`` except ``nums[i]``.

        Raises:
            ValueError: If ``nums`` is empty.

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
