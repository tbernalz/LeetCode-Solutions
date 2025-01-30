class Solution:
    def maxValue(self, n: str, x: int) -> str:
        """
        Maximizes the numerical value of a large integer 'n' (as a string) by inserting digit 'x'.
        For negative numbers, 'x' cannot be inserted to the left of the negative sign.

        Args:
            n (str): The large integer represented as a string. Can be positive or negative.
            x (int): The digit to insert into 'n'. Must be in the range [1, 9].

        Returns:
            str: The string representation of the maximum value of 'n' after inserting 'x'.
        """
        is_negative = n[0] == "-"

        for i in range(len(n)):
            if is_negative:
                if i > 0 and int(n[i]) > x:
                    return n[:i] + str(x) + n[i:]
            else:
                if int(n[i]) < x:
                    return n[:i] + str(x) + n[i:]  # n.insert(str(x))

        return n + str(x)
