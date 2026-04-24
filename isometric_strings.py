class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        len_s = len(s) 
        len_t = len(t)
        s_mapping = {}
        t_mapping = {}

        rc = False
        if len_s == len_t:

            for i in range(len_s):
                s_mapping[s[i]] = t[i]
                t_mapping[t[i]] = s[i]
            
            temp_s = ""
            temp_t = ""
            for i in range(len_s):
                temp_t += s_mapping[s[i]]
                temp_s += t_mapping[t[i]]
        
            rc = (temp_t == t) and (temp_s == s)

        return rc    
