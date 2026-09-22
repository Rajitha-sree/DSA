class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        rev = 0
        while x>0:
            rev = rev*10 + (x%10)
            x= x//10

        if temp == rev:
            return True
        return False
        