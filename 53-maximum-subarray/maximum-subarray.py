class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c_sum = 0
        b_sum = 0

        if (all(x<0 for x in nums)):
            return max(nums)
        else:
            for i in nums:
                c_sum = max(i,c_sum+i)
                b_sum = max(c_sum,b_sum)

            return b_sum
        
        