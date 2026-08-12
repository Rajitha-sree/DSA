class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(people)
        l = 0 
        r = n-1
        count = 0
        people.sort()
        while l<=r:
            if people[l]+people[r] <= limit:
                count+=1
                l+=1
                r-=1
            else:
                count+=1
                r-=1

        return count
        