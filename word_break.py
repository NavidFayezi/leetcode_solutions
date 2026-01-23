class Solution:
    """Word Break solution.

    Determines if a string can be segmented into words from a dictionary
    using a BFS-like approach to explore all valid prefixes.
    """

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """Check if string s can be segmented into words from wordDict.

        Args:
            s (str): The input string to segment.
            wordDict (list[str]): List of valid words that can be used to
                construct the string.

        Returns:
            bool: True if s can be segmented into a sequence of one or more
                dictionary words, False otherwise.

        """
        temp_list = [""]
        set_of_candidates = set()

        while True:
            new_candidates_list = []
            for candidate in temp_list:
                for word in wordDict:
                    new_candidate = candidate + word
                    if new_candidate == s:
                        return True
                    if (
                        s[: len(new_candidate)] == new_candidate
                        and new_candidate not in set_of_candidates
                    ):
                        new_candidates_list.append(new_candidate)
                        set_of_candidates.add(new_candidate)

            if len(new_candidates_list) == 0:
                break
            else:
                temp_list = new_candidates_list[:]
        return False