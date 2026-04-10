import math 


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        return self.binary_search_window_size(target, nums)

    def binary_search_window_size(self, target: int, nums: list[int]):
        array_len = len(nums)
        min_window = math.inf
        window_low = 1

        # add one because (a + (a+1)) // 2 never results in a+1
        window_up = array_len + 1

        while True:
            window_size = (window_up + window_low) // 2
            beginning = 0
            end = 0
            target_met = False

            sub_array_sum = 0
            while end < array_len:
                sub_array_sum += nums[end]
                if sub_array_sum >= target:
                    min_window = min(min_window, window_size)
                    target_met = True
                    break
                else:
                    if end - beginning + 1 == window_size:
                        sub_array_sum -= nums[beginning]
                        end += 1
                        beginning += 1
                    else:
                        end += 1

            if target_met == True:
                if window_size == window_low:
                    break
                else:
                    window_up = window_size
            
            if target_met == False:
                if window_size == window_low:
                    break
                else:
                    window_low = window_size
        if min_window == math.inf:
            return 0
        else:
            return min_window
