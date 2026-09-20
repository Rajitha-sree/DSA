class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0
        for i in range(n):
            c = 0
            while(nums[i]>0):
                c+=1
                nums[i]=nums[i]//10
            if(c%2==0):
                count+=1
        
        return count