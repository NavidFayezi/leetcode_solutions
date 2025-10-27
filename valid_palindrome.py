class Solution:
    def isPalindrome(self, s: str) -> bool:
        beginning = 0
        end = len(s) - 1
        is_palindrome = True
        while beginning < end:
            # for some weird reason when I use python's built-in string 
            # manipulation functions, it takes longer for the code to 
            # execute
            left_order = ord(s[beginning])
            right_order = ord(s[end])
            
            if 65 <= left_order <= 90:
                left_order += 32
            
            if 65 <= right_order <= 90:
                right_order += 32
            
            if (left_order < 97 or left_order > 122) and (left_order < 48 or left_order > 57):
                beginning += 1
                continue
            
            if (right_order < 97 or right_order > 122) and (right_order < 48 or right_order > 57):
                end -= 1
                continue

            if right_order != left_order:
                is_palindrome = False
                break
            else:
                beginning += 1
                end -= 1

        return is_palindrome
            

if __name__ == "__main__":
    test_input = "poliilop"
    solution = Solution()
    print(solution.isPalindrome(test_input))

