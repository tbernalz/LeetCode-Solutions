from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        """
        Calculates the number of unique xor triplets that are on an array.
        A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k]
        where i <= j <= k.

        Args:
            nums (List[int]): A integer array of permutations of the numbers in the range [1, len(nums)].

        Returns:
            int: The number of unique xor triplets.
        """
        n = len(nums)
        count = 0

        if n <= 2:
            return n

        while n > 0:
            count += 1
            n = n // 2

        return pow(2, count)
