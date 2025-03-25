class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        1. Find the first overlapping interval with newInterval
        2. Merge coming intervals until not
        3. Finally insert and return the new intervals

        Three scenairos:
         1 - ..()[]..
         2 - ..([])..
         3 - ..[()].. 
         4 - ..([)]..
         5 - ..[(])..
         6 - ..[]()..
        """

        updatedIntervals = []
        i, N = 0, len(intervals)


        while i < N:
            if intervals[i][1] >= newInterval[0]:
                break

            updatedIntervals.append(intervals[i])
            i += 1

        start, end = newInterval

        while i < N and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        updatedIntervals.append([start, end])

        while i < N:
            updatedIntervals.append(intervals[i])
            i += 1

        return updatedIntervals
