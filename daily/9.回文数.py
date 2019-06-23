'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 双指针法
        s = str(x)
        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True