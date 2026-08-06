class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = [0]*len(nums)
        l = 0
        r = len(nums)-1
        k = len(nums)-1
        while(k>=0):
            if abs(nums[l])<abs(nums[r]):
                a[k] = nums[r]*nums[r]
                r-=1
                k-=1
            else:
                a[k] = nums[l]*nums[l]
                l+=1
                k-=1


        return a