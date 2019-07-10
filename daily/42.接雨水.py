'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
'''


# dp，整体思路是将左右两边最大的值记录在新生成的列表中，然后计算
class Solution:
    def trap(self, height: [int]) -> int:
        len_ = len(height)
        if len_ < 3:
            return 0
        res = 0
        left = [0] * len_
        right = [0] * len_

        left[0] = height[0]
        right[-1] = height[-1]
        for i in range(1 ,len_):
            left[i] = max(left[ i -1] ,height[i])

        for i in range(len_ - 2 ,-1 ,-1):
            right[i] = max(right[ i +1] ,height[i])

        for i in range(len_):
            res += min(right[i] ,left[i]) - height[i]

        return res