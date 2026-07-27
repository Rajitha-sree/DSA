class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pf = []
        sum = 0
        for i in nums:
            sum += i
            pf.append(sum)

        n = len(nums)
        total = pf[n-1]

        for i in range(len(nums)):
            left_sum = pf[i-1] if i> 0 else 0
            right_sum = total-pf[i]
            if left_sum == right_sum:
                return i

        return -1
                

        