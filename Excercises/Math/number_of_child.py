class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        """
        Determines which child has the ball after a given number of seconds.

        Args:
            n(int): The number of children in the circle.
            k(int): The number of seconds the ball is passed around.

        Returns:
            int: The number of the child who receives the ball after the given seconds.
        """
        cycle_length = max(1, (n * 2) - 2)

        position = k % cycle_length

        while position >= n:
            position -= cycle_length

        return abs(position)
