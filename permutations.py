class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(res, nums, [])
        return res

    def backtrack(
        self, result: List[List[int]], nums: List[int], path: List[int]
    ):
        if nums == []:
            result.append(path[:])
            return None
        else:
            nums_len = len(nums)

            for i in range(nums_len):
                path.append(nums[i])
                temp = nums[:i] + nums[i + 1 :]
                self.backtrack(result, temp, path)
                path.pop()

            return None
