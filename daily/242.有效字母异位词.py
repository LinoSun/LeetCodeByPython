'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false

可以假设所有字母都是小写字母
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {'a' :0 ,'b' :0 ,'c' :0 ,'d' :0 ,'e' :0 ,'f' :0 ,'g' :0,
               'h' :0 ,'i' :0 ,'j' :0 ,'k' :0 ,'l' :0 ,'m' :0 ,'n' :0,
               'o' :0 ,'p' :0 ,'q' :0 ,'r' :0 ,'s' :0 ,'t' :0 ,'u' :0,
               'v' :0 ,'w' :0 ,'x' :0 ,'y' :0 ,'z' :0,
               }

        for v in s:
            dic[v] += 1

        for v in t:
            dic[v] -= 1

        for v in dic.values():
            if v != 0:
                return False

        return True