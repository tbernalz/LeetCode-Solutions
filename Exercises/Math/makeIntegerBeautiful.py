class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        """
        Find the smallest non-negative integer `x` such that the sum of the digits of `n + x` is <= `target`.

        Args:
            n (int): The integer to be modified.
            target (int): The maximum allowed sum of digits for `n + x`.

        Returns:
            int: The smallest `x` such that the digit sum of `n + x` <= `target`.
        """

        def digits_sum(num: int) -> int:
            sum = 0
            while num:
                digit = num % 10
                num = num // 10
                sum += digit

            return sum

        x = 0
        units = 10
        while digits_sum(n) > target:
            remainder = n % units
            increment = units - remainder
            n += increment
            x += increment
            units *= 10

        return x
