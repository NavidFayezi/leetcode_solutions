class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = dict()
        nums_len = len(nums)
        for i in range(nums_len):
            if nums[i] in nums_dict:
                if abs(nums_dict[nums[i]] - i) <= k:
                    return True
                else:
                    nums_dict[nums[i]] = i
            else:
                nums_dict[nums[i]] = i
        return False
