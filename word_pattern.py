class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        no_words = len(words)
        if no_words != len(pattern):
            return False
        
        mapping_s = {}
        mapping_pattern = {}
        rc = True
        for i in range(no_words):
            if pattern[i] not in mapping_pattern:
                mapping_pattern[pattern[i]] = words[i]
            else:
                if mapping_pattern[pattern[i]] != words[i]:
                    rc = False
                    break

            if words[i] not in mapping_s:
                mapping_s[words[i]] = pattern[i]
            else:
                if mapping_s[words[i]] != pattern[i]:
                    rc = False
                    break
        return rc
