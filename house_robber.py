class Solution:
    def rob(self, nums: list[int]) -> int:
        list_length = len(nums)
        table = [0 for i in range(list_length + 1)] # padding is required
        table[0] = 0
        table[1] = nums[0]

        for i in range(2, list_length + 1):
            table[i] = max(table[i - 1], table[i - 2] + nums[i - 1])
        
        return table[-1]
        