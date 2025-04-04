from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
            Inserts a new interval into a list of non-overlapping intervals, merging overlaps if necessary.

        Args:
            intervals (List[List[int]]): A list of non-overlapping intervals, where each interval is represented as [start_i, end_i].
                                         The list is sorted in ascending order based on `start_i`.
            newInterval (List[int]): The new interval to insert, represented as [start, end].

        Returns:
            List[List[int]]: A new list of intervals after insertion and merging, maintaining the non-overlapping and sorted properties.
        """
        intervals_fixed = []
        inserted = False

        for interval in intervals:
            if interval[1] < newInterval[0]:
                intervals_fixed.append(interval)
            elif interval[0] > newInterval[1]:
                if not inserted:
                    intervals_fixed.append(newInterval)
                    inserted = True
                intervals_fixed.append(interval)
            else:
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1]),
                ]

        if not inserted:
            intervals_fixed.append(newInterval)

        return intervals_fixed
