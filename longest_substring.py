class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        beginning = 0
        end = 0
        string_len = len(s)
        letter_to_index = {}
        longest_substring_length = 0
        while end < string_len:
            if s[end] not in letter_to_index \
               or letter_to_index[s[end]] < beginning:

                letter_to_index[s[end]] = end
                end += 1

            else:
                longest_substring_length = max(
                                                longest_substring_length, 
                                                (end - beginning)
                                            )
                beginning = letter_to_index[s[end]] + 1
                letter_to_index[s[end]] = end
                end += 1
        
        return max(longest_substring_length, (end - beginning))
