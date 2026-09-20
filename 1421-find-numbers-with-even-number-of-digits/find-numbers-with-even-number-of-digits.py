class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0
        for i in nums:
            c = 0
            while(i>0):
                c+=1
                i=i//10
            if(c%2==0):
                count+=1
        
        return count