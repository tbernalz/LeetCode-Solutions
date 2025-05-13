class Solution:
    def alternateDigitSum(self, n: int) -> int:
        """
        Calculate the alternate digit sum of a given integer.
        The alternate digit sum should follow these rules:
            - The most significant digit is assigned a positive sign.
            - Each other digit has an opposite sign to its adjacent digits.

        Args:
            n (int): A positive integer to analyze.

        Returns:
            int: The result of the alternate digit sum.
        """
        result = 0
        n_str = str(n)

        for i, num_char in enumerate(n_str):
            digit = int(num_char)
            result += digit if i % 2 == 0 else -digit

        return result
