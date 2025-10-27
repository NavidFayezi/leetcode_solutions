class Solution:
    def reverseWords(self, s: str) -> str:
        """Reverse the order of words in a string.

        Given a string ``s`` containing words separated by spaces, return a
        new string with the words in reverse order. Consecutive spaces are
        treated as a single separator and leading/trailing spaces are removed
        in the result.

        Args:
            s (str): Input string containing words separated by spaces.

        Returns:
            str: A string with the words in reversed order and a single space
                separating words.

        Example:
            >>> Solution().reverseWords("the sky is blue")
            "blue is sky the"
        """
        s = s.split(" ")
        res = ""
        for word in s:
            if word != "":
                res = " " + word + res

        return res[1:]

if __name__ == "__main__":
    test_input = "the sky is blue"
    solution = Solution()
    print(solution.reverseWords(test_input))