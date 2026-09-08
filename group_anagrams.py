class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        for _string in strs:
            sorted_strs.append(''.join(sorted(_string)))
        
        groups = dict()
        strs_len = len(strs)
        for i in range(strs_len):
            if sorted_strs[i] in groups:
                groups[sorted_strs[i]].append(strs[i])
            else:
                groups[sorted_strs[i]] = [strs[i]]
        
        results = list(groups.values())
        return results
