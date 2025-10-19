class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_product = [1]
        
        # right_product should be reversed at the end of the loop
        right_product = [1]
        list_length = len(nums)

        for i in range(1, list_length):
            left_product.append(left_product[-1] * nums[i - 1])
            right_product.append(right_product[-1] * nums[list_length - i])

        right_product = right_product[::-1]
        
        # a list whose ith element is the product of all elements in nums
        # except for nums[i]
        answer = []
        for i in range(list_length):
            answer.append(left_product[i] * right_product[i])
        
        return answer


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4]
    print(solution.productExceptSelf(nums))  # Output: [24, 12, 8, 6]
