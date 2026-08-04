class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        max_area = 0
        r = len(height) - 1
        while l<r:
            area =  min(height[l],height[r]) * (r-l)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1

            max_area = max(area,max_area)

        return max_area

        