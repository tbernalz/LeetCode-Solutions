class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Calculates the number of set bits in the binary representation of a positive integer.

        Args:
            n(int): The positive number to check.

        Returns:
            int: The number of set bits (Hamming weight).
        """
        weight = 0

        while n > 0:
            weight += n & 1
            n >>= 1
        return weight
