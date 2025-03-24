class Solution:
    def calculate(self, s: str) -> int:
        """
        Calculates the result of a mathematical expression given as a string.
        The expression may contain digits, '+', '-', '*', '/' with no parentheses.

        Args:
            s (str): The mathematical expression.

        Returns:
            int: The computed result.
        """
        expression = s.replace(" ", "")
        stack = []
        operation = "+"
        num = 0

        for i, char in enumerate(expression):
            if char.isdigit():
                num = int(str(num) + char)

            if not char.isdigit() or i == len(expression) - 1:
                if operation == "+":
                    stack.append(num)
                elif operation == "-":
                    stack.append(-num)
                elif operation == "*":
                    stack.append(stack.pop() * num)
                elif operation == "/":
                    stack.append(int(stack.pop() / num))

                operation = char
                num = 0

        return sum(stack)
