class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res = []
        beginning = 0
        end = 0
        array_len = len(nums)

        for i in range(0, array_len):
            if i < array_len - 1 and nums[i] == nums[i + 1] - 1:
                end += 1
                
            else:
                if beginning == end:
                    temp = str(nums[beginning])

                else:
                    temp = "" + str(nums[beginning]) + "->" + str(nums[end])

                beginning = i + 1
                end = i + 1
                res.append(temp)

        return res
    