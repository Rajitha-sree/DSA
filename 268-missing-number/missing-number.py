class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        n = len(nums)
        expected = (n * (n+1))//2
        for i in range(len(nums)):
            sum += nums[i]

        return expected-sum


        