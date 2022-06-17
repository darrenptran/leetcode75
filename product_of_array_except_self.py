class Solution:
    def productExceptSelf(self, nums):

        prod_before_idx = [1]*len(nums)
        prod_after_idx = [1]*len(nums)
        before_times_after = [0]*len(nums)

        for i in range(1, len(nums)):
            prod_before_idx[i] = prod_before_idx[i-1]*nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            prod_after_idx[i] = prod_after_idx[i+1]*nums[i+1]

        for i in range(0, len(nums)):
            before_times_after[i] = prod_before_idx[i]*prod_after_idx[i]

        return before_times_after