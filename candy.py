class Solution:
    def candy(self, ratings: list[int]) -> int:
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