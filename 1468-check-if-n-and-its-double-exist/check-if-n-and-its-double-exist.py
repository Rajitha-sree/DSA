class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        for i in range(n):
            for j in range(n):
                if(i!=j):
                    if(arr[i] == 2*arr[j]):
                        return True

        return False
        