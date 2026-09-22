class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        rev = 0
        if x <0:
            flag =1

        n = abs(x)
        while n>0:
            rev = rev*10+n%10
            n = n//10
        if rev < -2147483648 or rev > 2147483647:
            return 0
        if(flag==1):
            return -rev
        else:
            return rev


        