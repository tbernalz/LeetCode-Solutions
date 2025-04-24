class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        Calculate the minimum deletions needed to make a binary string balanced.
        A string is balanced when there are no 'b's followed by 'a's.

        Args:
            s (str): A string consisting only of 'a' and 'b' characters

        Returns:
            int: The minimum number of deletions required to balance the string.
        """
        min_deletions = 0
        count_b = 0

        for char in s:
            if char == "b":
                count_b += 1
            else:
                min_deletions = min(min_deletions + 1, count_b)

        return min_deletions
