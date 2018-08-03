# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda _:_.start)
        ret = [intervals[0]]
        for _ in intervals:
            if ret[-1].end >= _.start:
                ret[-1].end = max(_.end, ret[-1].end)
            else:
                ret.append(_)
        return ret