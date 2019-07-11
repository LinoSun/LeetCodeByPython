'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''

#  code review第一遍
# 最简洁做法，也是状态转换点
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
        return max(nums)



# 比较容易理解的动态规划，但是状态转换点不理解
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        if max(nums) < 0:
            return max(nums)

        local_max, global_max = 0, 0

        for num in nums:
            local_max = max(0, local_max + num)
            global_max = max(local_max, global_max)

        return global_max