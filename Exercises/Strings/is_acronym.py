class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        """
        Determine if a word is an acronym for all the words in an array.

        Args:
            words(list[str]): The array containing the words to check.
            s(str): The word to check as an acronym.

        Returns:
            bool: True if the word is an acronym, False otherwise.
        """
        return s == "".join(word[0] for word in words)
