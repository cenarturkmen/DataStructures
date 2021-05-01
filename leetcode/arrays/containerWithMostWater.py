#https://leetcode.com/problems/container-with-most-water/
# o(n) time complexity
def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
    l = 0
    r = len(height)-1
    cur = 0
    maxsf = 0
        
    while l<r:
        cur = (r-l) * min(height[l], height[r])
        maxsf = max(maxsf, cur)
        if height[l]>=height[r]:
            r = r -1
                
        else:
            l = l + 1
                
    return maxsf
        