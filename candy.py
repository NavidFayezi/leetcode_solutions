class Solution:
    def candy(self, ratings: list[int]) -> int:
        """Compute the minimum number of candies needed.

        The method implements a two-pass greedy algorithm:
        1. Initialize each child with one candy.
        2. Iterate left-to-right and increment candies when a child has a
           higher rating than the right neighbor but not more candies.
        3. Reverse the `ratings` and `candies` lists and repeat the same
           process to ensure the right-to-left constraint holds.

        Args:
            ratings (list[int]): A list of integers representing the rating of
                each child. Length may not be zero.

        Returns:
            int: The minimum total number of candies required to satisfy the
                problem constraints.

        Raises:
            None: This function does not raise for valid input. If non-list
                types are passed, a TypeError may be raised by native
                operations.

        Complexity:
            Time: O(n) where n = len(ratings).
            Space: O(n) for the intermediate `candies` list.
        """
        array_length = len(ratings)
        candies = [1 for i in range(array_length)]

        for i in range(array_length - 1):
            if (ratings[i] > ratings[i + 1]) and (candies[i] <= candies[i + 1]):
                candies[i] = candies[i + 1] + 1
            elif (ratings[i] < ratings[i + 1]) and (
                candies[i] >= candies[i + 1]
            ):
                candies[i + 1] = candies[i] + 1

        candies = candies[::-1]
        ratings = ratings[::-1]
        for i in range(array_length - 1):
            if (ratings[i] > ratings[i + 1]) and (candies[i] <= candies[i + 1]):
                candies[i] = candies[i + 1] + 1
            if ratings[i] < ratings[i + 1] and candies[i] >= candies[i + 1]:
                candies[i + 1] = candies[i] + 1

        return sum(candies)


if __name__ == "__main__":

    test_input = [1, 3, 4, 5, 2]
    solver = Solution()
    print(solver.candy(test_input))