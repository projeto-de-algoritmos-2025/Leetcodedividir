class Solution:
    def maxSubArray(self, nums):
        def helper(left, right):
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            left_sum = helper(left, mid)
            right_sum = helper(mid + 1, right)
            cross_sum = self.maxCrossingSum(nums, left, mid, right)
            return max(left_sum, right_sum, cross_sum)

        return helper(0, len(nums) - 1)

    def maxCrossingSum(self, nums, left, mid, right):
        left_sum = float('-inf')
        total = 0
        for i in range(mid, left - 1, -1):
            total += nums[i]
            left_sum = max(left_sum, total)

        right_sum = float('-inf')
        total = 0
        for i in range(mid + 1, right + 1):
            total += nums[i]
            right_sum = max(right_sum, total)

        return left_sum + right_sum
