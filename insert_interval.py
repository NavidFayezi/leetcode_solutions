class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if intervals == []:
            return [newInterval]

        i = 0
        len_intervals = len(intervals)
        if newInterval[0] < intervals[0][0]:
            intervals = [newInterval] + intervals[:]
        else:
            while i < len_intervals - 1:
                if intervals[i][0] <= newInterval[0] \
                and intervals[i + 1][0] > newInterval[0]:
                    break
                else:
                    i += 1
            intervals = intervals[: i + 1] + [newInterval] + intervals[i + 1:]
        len_intervals += 1

        to_be_removed = set()
        while i < len_intervals - 1:
            if intervals[i][1] < intervals[i + 1][0]:
                pass

            else:
                intervals[i + 1][0] = min(intervals[i][0], intervals[i + 1][0])
                intervals[i + 1][1] = max(intervals[i][1], intervals[i + 1][1])
                to_be_removed.add(i)
            i += 1
        res = []
        for j in range(len_intervals):
            if j in to_be_removed:
                pass
            else:
                res.append(intervals[j])
        return res
