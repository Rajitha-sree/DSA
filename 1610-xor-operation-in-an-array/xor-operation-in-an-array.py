class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        y = 0
        for i in range(0,n):
            x = start + 2*i
            y = y^x

        return y
        