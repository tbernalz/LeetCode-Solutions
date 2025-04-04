# Insert Interval

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/insert-interval/description/).

## Initial Approach

The initial approach involves iterating through the existing intervals while intelligently merging the `newInterval` where necessary. The algorithm processes each interval in the sorted list and checks for overlaps with `newInterval`.

1. **Non-overlapping intervals before `newInterval`**:

   - If an interval ends before `newInterval` starts, it is added to the result as-is since no overlap exists.

1. **Overlapping intervals**:

   - If an interval overlaps with `newInterval`, they are merged by taking the minimum of the start times and the maximum of the end times.

1. **Non-overlapping intervals after `newInterval`**:

   - Once all overlapping intervals are merged, the remaining intervals that start after the merged `newInterval` are added to the result.

1. **Insertion of `newInterval` if not yet placed**:

   - If `newInterval` was not merged with any existing interval and no interval appears after it without overlap, it is appended at the end.

This approach efficiently merges intervals in a single pass while maintaining the sorted order.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the array

- **Space Complexity**: `O(n)`, where n is the length of the array
