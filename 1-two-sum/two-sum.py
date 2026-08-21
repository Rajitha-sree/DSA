class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # a = []
        # for l in range(len(nums)):
        #     for r in range(l+1,len(nums)):
        #         if nums[l]+nums[r] == target:
        #             a.append(l)
        #             a.append(r)

        #             return a

        # a = []
        # for l in range(len(nums)):
        #     r = target - nums[l]
        #     if r in nums:
        #         i = nums.index(r)
        #         if i!=l:
        #             a.append(l)
        #             a.append(i)

        #             return a
                
        dict = {}

        
        for i in range(len(nums)):
            req = target - nums[i]
            if req in dict and dict[req]!=i:
                return [dict[req],i]
            dict[nums[i]] = i
            
        return []
        