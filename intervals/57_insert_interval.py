'''You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

# Solution

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        output = []
        idx = 0
        # intervals is already sorted
        # add all elements in intervals that go before newInterval
        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            output.append(intervals[idx])
            idx += 1
        
        # hit overlap, add these overlapping elements
        while idx < len(intervals) and intervals[idx][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[idx][0])
            newInterval[1] = max(newInterval[1], intervals[idx][1])
            idx += 1
        output.append(newInterval)

        # add remaining elements that are bigger than the interval
        while idx < len(intervals):
            output.append(intervals[idx])
            idx += 1

        return output
