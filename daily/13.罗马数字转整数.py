'''
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''

# 罗马数字有规律，从左往右读
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        rs = dic[s[-1]]
        for i in range(len(s) - 1):
            if dic[s[i]] < dic[s[i + 1]]:
                rs -= dic[s[i]]
            else:
                rs += dic[s[i]]

        return rs