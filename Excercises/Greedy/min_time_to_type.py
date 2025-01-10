class Solution(object):
    def minTimeToType(self, word: str) -> int:
        """
        Calculate the minimum number of seconds to type a word on a circular typewriter.

        Args:
            word(str): The word to type.

        Returns:
            int: Minimum number of seconds to type the word.
        """
        seconds = 0
        current_position = 0

        for char in word:
            target_position = ord(char) - ord("a")
            distance = min(
                abs(current_position - target_position),
                26 - abs(current_position - target_position),
            )
            seconds += distance + 1
            current_position = target_position

        return seconds
