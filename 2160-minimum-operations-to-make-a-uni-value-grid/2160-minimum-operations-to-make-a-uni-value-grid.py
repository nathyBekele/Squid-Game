class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        if len(grid) == 0:
            return 0

        ROW, COL = len(grid), len(grid[0])

        all_numbers = []

        for r in range(ROW):
            for c in range(COL):
                if len(all_numbers) != 0 and abs(grid[r][c] - all_numbers[-1])%x != 0:
                    return -1
                
                all_numbers.append(grid[r][c])

    
        all_numbers.sort()
        target = all_numbers[(ROW*COL)//2]

        print(all_numbers, target)

        min_ops = 0
        for num in all_numbers:
            min_ops += abs(num - target)

        return min_ops//x




        

