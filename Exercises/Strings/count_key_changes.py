class Solution:
    def countKeyChanges(self, s: str) -> int:
        """
        Calculates the number of times the input string changes "keys".

        Args:
            s(str): The string to analyze.

        Returns:
            int: The number of key changes.
        """
        key_changes = 0
        current_key = s[0].lower()

        for char in s[1:]:
            if char.lower() != current_key:
                key_changes += 1
                current_key = char.lower()

        return key_changes
