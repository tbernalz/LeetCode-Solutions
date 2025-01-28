class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        """
        Calculate the length of the longest uncommon subsequence between two strings.

        Args:
            a(str): The first string to analyze.
            b(str): The second string to analyze.

        Returns:
            int: The length of the longest uncommon subsequence between two strings, or -1 if no such uncommon subsequence exists.
        """
        if a == b:
            return -1
        else:
            return max(len(a), len(b))
