'''
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)

        for i in range(len(haystack) - l + 1):
            if haystack[i:i + l] == needle:
                return i
        return -1


# 利用python特性，手动斜眼写
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
