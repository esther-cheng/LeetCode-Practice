class Solution(object):
    def maxArea(self, height):
        ret = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r-l) * min(height[l], height[r])
            ret = max(area, ret)

            if height[l] < height[r]:
                l+=1
            elif height[r] < height[l]:
                r-=1
            else:
                l+=1
        
        return ret
  


        