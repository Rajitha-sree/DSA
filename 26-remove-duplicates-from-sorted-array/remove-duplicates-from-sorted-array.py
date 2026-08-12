class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # a = []
        # for i in nums:
        #     if i not in a:
        #         a.append(i)  
        # for i in range(len(a)):
        #     nums[i] = a[i]

        # return len(a)
        j = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[j]=nums[i]
                j+=1

        return j
