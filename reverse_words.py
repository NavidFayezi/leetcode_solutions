class Solution:
    def reverseWords(self, s: str) -> str:
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