class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        """
        Count the number of index pairs (i, j) such that i < j, and words[i] is both a prefix and a suffix of words[j].

        Args:
            words(List[str]): A list of words to analyze.

        Returns:
            int: The count of valid index pairs (i, j).
        """
        count = 0
        n = len(words)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    count += 1

        return count

    def isPrefixAndSuffix(self, prefix_suffix: str, word: str) -> bool:
        """
        Check if a string is both a prefix and a suffix of another string.

        Args:
            prefix_suffix(str): The string to check as a prefix and suffix.
            word(str): The string to validate against.

        Returns:
            bool: True if prefix_suffix is both a prefix and suffix of word, False otherwise.
        """
        length = len(prefix_suffix)
        return prefix_suffix == word[:length] and prefix_suffix == word[-length:]
