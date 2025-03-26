class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N, ans = len(grid), [0, 0]

        all_numbers = [False for _ in range(N*N + 1)]

        for r in range(N):
            for c in range(N):
                if all_numbers[grid[r][c]] == True:
                    ans[0] = grid[r][c]
                else:
                    all_numbers[grid[r][c]] = True

        for i in range(1, N*N + 1):
            if all_numbers[i] == False:
                ans[1] = i
                break

        return ans