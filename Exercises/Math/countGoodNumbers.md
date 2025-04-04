# Count Good Numbers

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/count-good-numbers/description/).

## Initial Approach

When I read the statement, I realized:

- Even positions (0, 2, 4, ...) can only be even digits (0, 2, 4, 6, 8) -> 5 choices.

- Odd positions (1, 3, 5, ...) can only be prime digits (2, 3, 5, 7) -> 4 choices.

So, for a string of length `n`:

- If `n = 1`, only the first digit (even index) matters → 5 possibilities.

- If `n = 2`, first digit (even index) has 5 choices, second (odd index) has 4 → total 5 × 4 = 20.

- If `n = 3`, it's 5 × 4 × 5 = 100, and so on.

This means the answer is just: **5 ^ number of even indices × 4 ^ number of odd indices**

This approach avoids brute force by directly computing the result using exponents, making it highly efficient for large `n`.

```Python
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even_count = (n + 1) // 2
        odd_count = n // 2

        return 5**even_count * 4**odd_count

```

## Optimized Solution

The problem requires the result modulo `(10 ^ 9 )+ 7` to prevent huge numbers. So, instead of computing `5 \*\* even_count` directly (which could be astronomically large), we use modular exponentiation (`pow(base, exp, mod)`).

This optimization:

- **Avoids integer overflow** (since Python can handle big numbers, but LeetCode expects modulo).

- **Speeds up computation** (modular exponentiation is much faster for large powers).

## Complexity

**Initial Approach**:

- **Time Complexity**: `O(log n)`, since the exponentiation operations take O(log n) time in Python.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.

**Optimized Solution**:

- **Time Complexity**: `O(log n)`, modular exponentiation with pow(a, b, mod) is done in O(log b) time in Python.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
