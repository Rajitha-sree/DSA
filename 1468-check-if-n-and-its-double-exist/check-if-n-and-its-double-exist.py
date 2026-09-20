class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        #Brute-force-approach
        # n = len(arr)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if(i!=j):
        #             if(arr[i] == 2*arr[j] or arr[j] == 2*arr[i]):
        #                 return True

        # return False

        #hash set
        seen = set()
        for i in arr:
            if(2*i in seen) or (i%2==0 and i//2 in seen):
                return True
            seen.add(i)

        return False
        