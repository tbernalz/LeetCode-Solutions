## Number of 1 Bits

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/number-of-1-bits/description/).

## Initial Approach

In my initial attempt, I approached the problem by manually simulating the binary representation of the number. Here's how I thought about it:

1. **Understand the Problem**:
   I knew I had to count the number of `1`s in the binary representation of the integer `n`. Since I wasn’t very familiar with bitwise operations initially, I focused on simulating the process using division by `2`.

1. **Divide and Count**:

   - Each division by `2` helps extract the binary digits of `n` one by one, starting from the least significant bit (LSB).
   - If n is divisible by `2`, the binary digit is `0`. If not, it’s `1`, and I increment the count (`weight`).

1. **Thought Process**:

   - I divided `n` by `2` in each iteration and checked if the result was a whole number. If not, it indicated a set bit (`1`).

   - I used a variable `weight` to count the number of `1`s and updated `n` to its integer division (`n // 2`) for the next iteration.

This approach worked, but it felt somewhat verbose and repetitive, and I suspected there was a more efficient way to solve it.

```Python
class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Calculates the number of set bits in the binary representation of a positive integer.

        Args:
            n(int): The positive number to check.

        Returns:
            int: The number of set bits (Hamming weight).
        """
        weight = 0

        while n > 0:
            temp_result = n / 2

            if temp_result % 1 == 0:
                n = temp_result

            else:
                weight += 1
                n = n // 2

        return weight

```

## Optimized Solution

While researching on LeetCode discussions, I learned about **bitwise operations**, which simplify this problem significantly. Here's how I arrived at the optimized solution:

1. **Use & for Set Bits**:

   - The expression `n & 1` isolates the least significant bit (LSB) of `n`. If the result is `1`, it means the LSB is set, and we increment `weight`.
   - This operation is faster and more direct than simulating division and checking remainders.

1. **Shift Right**:

   - Instead of dividing `n` by `2`, we can use `n >>= 1`, which shifts the binary representation of `n` one bit to the right. This is more efficient and directly removes the LSB.

1. **Why This is Better**:

   - The optimized solution is concise, uses fewer lines of code, and leverages Python's bitwise operators for better performance.
   - It avoids unnecessary conditionals and focuses directly on the problem of counting `1`s.

## Complexity

**Initial Approach**:

- **Time Complexity**: `O(log(n))`, where n is the number given.

   - The O(log(n)) comes because in each iteration of the `while` loop, it divides `n` by `2`. This reduces the size of `n` exponentially, and the number of iterations required is proportional to the number of bits in the binary representation of `n`.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.

**Optimized Solution**:

- **Time Complexity**: `O(log(n))`, where n is the number given.
- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
