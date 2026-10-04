class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        y = 0
        for i in range(n):
            x = start + 2*i
            y ^= x

        return y
        