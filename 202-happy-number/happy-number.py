class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def num(n):
            sum = 0
            while n>0:
                rem = n%10
                n = n//10
                sum+=rem*rem
            return sum
        seen = set()
        if n==1:
            return True
        while n!=1:
            n = num(n)
            if n in seen:
                return False
            else:
                if n == 1:
                    return True
                else:
                    seen.add(n)

                