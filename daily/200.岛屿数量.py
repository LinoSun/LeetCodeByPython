'''
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3
'''

# 回看代码
class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        p = set()
        flag = [[0 for i in range(n)] for j in range(m)]
        count = 0
        for i in range(m):
            if grid[i][0] == "1":
                count += 1
                flag[i][0] = count
                if i > 0 and flag[i - 1][0] > 0:
                    p.add((flag[i - 1][0], count))
            for j in range(1, n):
                if grid[i][j] == "0": continue

                if flag[i][j - 1]:
                    flag[i][j] = flag[i][j - 1]
                else:
                    count += 1
                    flag[i][j] = count
                if i > 0 and flag[i - 1][j]:
                    p.add((flag[i - 1][j], count))

        def union(a, b, par):
            while par[a] > 0:
                a = par[a]
            while par[b] > 0:
                b = par[b]

            if a != b:
                par[a] = b

        ans = [-1 for i in range(count + 1)]
        for i in p:
            union(i[0], i[1], ans)

        res = 0
        for i in range(1, count + 1):
            if ans[i] < 0:
                res += 1
        return res