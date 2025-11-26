class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        str_len = len(t)
        str_pointer = 0
        subsequence_len = len(s)
        sub_pointer = 0

        if subsequence_len == 0:
            return True

        if str_len == 0:
            return False

        while str_pointer < str_len:
            if t[str_pointer] == s[sub_pointer]:
                sub_pointer += 1
                if sub_pointer >= subsequence_len:
                    break
            
            str_pointer += 1

        return sub_pointer >= subsequence_len
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.isSubsequence(t="ahbgdc", s="abc"))