class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        cand = None
        count = 0

        for i in nums:
            if i == cand:
                count+=1
            elif count == 0:
                cand = i
                count=1
            else:
                count-=1

        return cand
        