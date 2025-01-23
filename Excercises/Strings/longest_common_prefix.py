class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """Finds the longest common prefix among an array of strings.

        Args:
            strs(list[str]): The list of strings to analize.

        Returns:
            str: The longest common prefix. Returns an empty string ("") if no common prefix exists.
        """
        longest_prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(longest_prefix):
                longest_prefix = longest_prefix[:-1]
                if not longest_prefix:
                    return ""

        return longest_prefix
