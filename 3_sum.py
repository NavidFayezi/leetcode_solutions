class Solution:
    """Find unique triplets that sum to zero.

    Implements a two-pointer sweep over a sorted copy of the input to collect
    all unique triplets (a, b, c) such that a + b + c == 0. Duplicates are
    prevented by storing triplets in a set during construction.

    Complexity
    - Time: O(n^2), dominated by the nested two-pointer search for each pivot.
    - Space: O(n) for the sorted copy of the input and the answer set.
    """

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Return all unique triplets whose sum is zero.

        Args:
            nums (list[int]): Input list of integers (may contain duplicates).

        Returns:
            list[list[int]]: List of unique triplets [a, b, c] such that
            a + b + c == 0. Triplets have no guaranteed ordering beyond what
            the algorithm produces.
        """
        len_nums = len(nums)
        sorted_list = sorted(nums)
        answers = set()

        for i in range(len_nums):
            left = i + 1
            right = len_nums - 1
            target = -1 * sorted_list[i]
            while left < right:

                temp = sorted_list[left] + sorted_list[right]
                if temp == target:
                    candidate = [
                        sorted_list[i],
                        sorted_list[left],
                        sorted_list[right],
                    ]
                    candidate = tuple(candidate)
                    left += 1
                    right -= 1
                    if candidate not in answers:
                        answers.add(candidate)
                elif temp < target:
                    left += 1
                else:
                    right -= 1

        list_answers = []
        for member in answers:
            list_answers.append(list(member))
        return list_answers
