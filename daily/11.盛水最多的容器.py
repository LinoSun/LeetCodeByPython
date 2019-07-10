'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
'''

# 第一种python特性写法，但是运行用时长
class Solution:
    def maxArea(self, height: [int]) -> int:
        tmp, l, r = 0, 0, len(height) - 1

        while l < r:
            tmp, l, r = (max(tmp, min(height[l], height[r]) * (r - l)), l + 1, r) if height[l] < height[r] else (
            max(tmp, min(height[l], height[r]) * (r - l)), l, r - 1)

        return tmp

# 可读性更高一点的
class Solution:
    def maxArea(self, height: [int]) -> int:

        tmp, l, r = 0, 0, len(height) - 1

        while l < r:
            lo = r - l
            if height[l] < height[r]:
                h = height[l]
                l += 1
            else:
                h = height[r]
                r -= 1
            area = h * lo
            if area > tmp:
                tmp = area

        return tmp


nums = [1,8,6,2,5,4,8,3,7]
s = Solution()
print(s.maxArea(nums))