from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        """
        Find all peaks in the given mountain array.

        A peak is defined as an element that is strictly greater than its immediate
        neighboring elements (i.e., the elements to its left and right). The first and
        last elements of the array cannot be peaks since they do not have two neighbors.

        Args:
            mountain (List[int]): A list of integers representing the mountain array.

        Returns:
            List[int]: A list of indices where peaks occur. The indices are 0-based and
                       can be returned in any order.
        """
        if len(mountain) < 3:
            return []

        peaks = []

        for i in range(1, len(mountain) - 1):
            if mountain[i - 1] < mountain[i] > mountain[i + 1]:
                peaks.append(i)

        return peaks
