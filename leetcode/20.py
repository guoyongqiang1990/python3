'''给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

'''


# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda l: l.start)
        new_tail = 0
        for interval in intervals:
            if interval.start > intervals[new_tail].end:
                new_tail += 1
                intervals[new_tail] = interval
            else:
                intervals[new_tail].end = max(interval.end, intervals[new_tail].end)
        return intervals[:new_tail + 1]





intervals = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]
lists = [[1,3],[2,6],[8,10],[15,18]]
s = Solution()
print(s.merge(intervals))