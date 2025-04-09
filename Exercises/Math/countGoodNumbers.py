class Solution:
    def countGoodNumbers(self, n: int) -> int:
        """
        Counts the total number of good digit strings of length n.

        A digit string is good if:
        - Digits at even indices (0-based) are even (0, 2, 4, 6, or 8)
        - Digits at odd indices are prime (2, 3, 5, or 7)

        Args:
            n (int): The length of the digit strings to count.

        Returns:
            int: The number of good digit strings of length n modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        even_count = (n + 1) // 2
        odd_count = n // 2

        return (pow(5, even_count, MOD) * pow(4, odd_count, MOD)) % MOD
