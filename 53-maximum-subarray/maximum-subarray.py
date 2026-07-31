class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        pref_sum = 0
        max_sum = nums[0]
        for i in nums:
            pref_sum += i
            max_sum = max(max_sum,pref_sum)
            if pref_sum < 0:
                pref_sum = 0
        
        return max_sum