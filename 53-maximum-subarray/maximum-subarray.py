class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hm = {0:-1}
        max_s = -2147483648
        pref_sum = 0
        prev_sum = 0
        for i in range(len(nums)):
            pref_sum += nums[i]
            max_s = max(pref_sum,max_s)
            if pref_sum < 0:
                pref_sum = 0
            # if pref_sum in hm:
            #     hm[pref_sum] += 1

        return max_s

        # pref_sum = 0
        # max_sum = 0
        # for i in nums:
        #     pref_sum += i
        #     max_sum = max(max_sum,pref_sum)
        #     if pref_sum < 0:
        #         pref_sum = 0
        
        # return max_sum