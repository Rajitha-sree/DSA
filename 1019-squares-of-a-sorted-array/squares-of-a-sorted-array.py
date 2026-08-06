class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []
        for i in nums:
            a.append(i*i)

        return sorted(a)