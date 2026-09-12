class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        nums_set = set()

        for number in nums:
            nums_set.add(number)
        
        res = 1
        for number in nums_set:
            if number - 1 in nums_set:
                continue
            
            current = number
            temp = 1
            while current + 1 in nums_set:
                current += 1
                temp += 1 
            res = max(temp, res)

        return res
