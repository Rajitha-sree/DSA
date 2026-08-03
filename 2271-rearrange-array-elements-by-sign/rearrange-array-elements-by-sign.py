class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = 0
        neg = 1
        n = len(nums)
        a = [0] * n
        for i in nums:
            if i>0:
                
                a[pos] = i
                pos+=2
            elif i<0:
                
                a[neg] = i
                neg+=2

        return a
            

        

        