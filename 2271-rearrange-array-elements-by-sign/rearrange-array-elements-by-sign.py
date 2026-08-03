class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = 0
        neg = 1
        n = 0
        a=[]
        for i in nums:
            if i>0:
                a.insert(pos,i)
                pos+=2
            elif i<0:
                a.insert(neg,i)
                neg+=2

        return a
            

        

        