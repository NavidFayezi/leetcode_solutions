class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_copy = t[:]
        last_index = len(s) - 1
        left = 0
        right = 0
        res = s[:]
        ans = False

        extras = dict()
        for character in t:
            extras[character] = 0
        
        while (t_copy == "" and left <= last_index) or (t_copy != "" and right <= last_index):
            if t_copy != "":
                is_in_t = t_copy.find(s[right])
                if is_in_t != -1:
                    t_copy = t_copy[:is_in_t] + t_copy[is_in_t + 1:]
                else:
                    if s[right] in extras:
                        extras[s[right]] += 1
                
                right += 1

            else:
                ans = True
                if right - left < len(res):
                    res = s[left : right]
                
                is_in_t = t.find(s[left])
                if (is_in_t > -1):
                    if extras[s[left]] == 0:
                        t_copy += s[left]
                    else:
                        extras[s[left]] -= 1

                left += 1
        
        if ans == False:
            res = ""
        return res
