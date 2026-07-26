class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.ps = []
        sum = 0
        for i in nums:
            sum = sum + i
            self.ps.append(sum)


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.ps[right]
        return self.ps[right]- self.ps[left-1]
        
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)