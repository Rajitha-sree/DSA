class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        k = 0
        p1 = len(s) - 1
        p2 = len(t) - 1
        while p1>=0 or p2>=0:
            while p1 >= 0:
                if s[p1] == '#':
                    p1-=1
                    k+=1
                elif k>0:
                    k-=1
                    p1-=1
                else:
                    break
            k=0
            while p2 >= 0:
                if t[p2] == '#':
                    p2-=1
                    k+=1
                elif k>0:
                    p2-=1
                    k-=1
                else:
                    break

                    
            if p1 >= 0 and p2 >= 0:
                if s[p1]!= t[p2]:
                    return False
            elif p1 >= 0 or p2 >= 0:
                return False
            p1-=1
            p2-=1
        return True 

            
        