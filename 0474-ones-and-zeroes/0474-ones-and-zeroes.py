class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        max_size, curr_size = 0, 0
        cache = defaultdict(int)

        def dp(i, m, n):
            nonlocal max_size
            if (i, m, n) in cache:
                return cache[(i, m, n)]
            
            if i >= len(strs) or (m <= 0 and n <= 0):
                return 0

            if strs[i][0] <= m and strs[i][1] <= n:
                cache[(i, m, n)] = max(cache[(i, m, n)], 1 + dp(i + 1, m - strs[i][0], n - strs[i][1]))
                
            cache[(i, m, n)] = max(cache[(i, m, n)], dp(i + 1, m, n))
            return cache[(i, m, n)]

        strs = [[num.count('0'), num.count('1')] for num in strs]

        return dp(0, m, n)


