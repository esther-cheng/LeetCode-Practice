class Solution(object):
    def findMin(self, nums):
        min = 5001

        for c in nums:
            if c < min:
                min = c

        return min  
        