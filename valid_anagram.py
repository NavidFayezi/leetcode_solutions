class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for character in alphabet:
            s_dict[character] = 0
            t_dict[character] = 0

        for character in s:
            s_dict[character] += 1

        for character in t:
            t_dict[character] += 1

        rc = True
        for character in alphabet:
            if s_dict[character] != t_dict[character]:
                rc = False
                break
        
        return rc
