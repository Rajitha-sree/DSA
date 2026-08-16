class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        l = 0
        r = 0
        while r<len(typed):
            if l<len(name) and name[l]== typed[r]:
                l+=1
            elif r==0 or typed[r]!=typed[r-1]:
                return False

            r+=1
        return l == len(name)