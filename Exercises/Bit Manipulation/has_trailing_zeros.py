class Solution:
    def hasTrailingZeros(self, nums: list[int]) -> bool:
        """
        Check if there are two or more elements in the array such that the bitwise OR of the selected elements has at least one trailing zero in its binary representation.

        Args:
            nums(list[int]): The array to analyze.

        Returns:
            bool: True if there are 2 or more elements in the array that accomplish the condition. False otherwise.
        """
        even_count = 0
        for num in nums:
            if num % 2 == 0:
                even_count += 1
                if even_count >= 2:
                    return True
        return False
