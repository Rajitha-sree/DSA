class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1

        for values in dict.values():
            if values >= 2:
                return True

        return False
        