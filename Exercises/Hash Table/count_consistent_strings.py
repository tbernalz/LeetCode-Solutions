class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        """
        Check how many strings in a list are made only of characters given by a string.

        Args:
            allowed(str): The string containing the allowed characters.
            words(List[str]): The list of strings to check.

        Returns:
            int: The number of strings from "words" that are made using only "allowed" characters.
        """
        characters_set = set(allowed)
        consistent_counter = 0

        for word in words:
            if all(char in characters_set for char in word):
                consistent_counter += 1

        return consistent_counter
