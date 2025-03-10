class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Guess a number between 1 and n using a binary search approach.

        Args:
            n (int): The upper bound of the range (1 to n) in which to guess the number.

        Returns:
            int: The number that was guessed correctly
        """

        def recursive_guess(start: int, end: int):
            mid = start + (end - start) // 2
            guess_result = guess(mid)
            if guess_result == 0:
                return mid
            elif guess_result == 1:
                return recursive_guess(mid + 1, end)
            else:
                return recursive_guess(start, mid - 1)

        return recursive_guess(0, n)
