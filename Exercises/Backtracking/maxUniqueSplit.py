class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        """
        Finds the maximum number of unique substrings that a given string can be split into.

        Args:
            s (str): A string.

        Returns:
            int: The maximum number of unique substrings.
        """

        def backtrack(start: int, seen: set[str]) -> None:
            nonlocal max_unique

            if start == len(s):
                max_unique = max(max_unique, len(seen))
                return

            for i in range(start + 1, len(s) + 1):
                substring = s[start:i]
                if substring not in seen:
                    seen.add(substring)
                    backtrack(i, seen)
                    seen.remove(substring)

        max_unique = 0
        backtrack(0, set())
        return max_unique
