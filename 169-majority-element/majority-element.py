class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #cand = nums[0]
        count = 0
        for i in range(len(nums)):
            if count == 0:
                cand =  nums[i]
                #count+=1
            if cand == nums[i]:
                count +=1
            elif cand != nums[i]:
                #cand = i
                count-=1

        return cand

        