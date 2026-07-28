class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        hm = {}
        p_sum = 0
        hm[0] = 1

        for i in range(len(nums)):
            p_sum += nums[i]
            prev_sum = p_sum - k
            
            if prev_sum in hm:
                count += hm[prev_sum]

            hm[p_sum] = hm.get(p_sum, 0) + 1
            
        return count
            
        
        return count