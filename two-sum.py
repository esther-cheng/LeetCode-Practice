class Solution(object):
    def twoSum(self, nums, target):
        mapofvals = {}

        for i in range(len(nums)):
            subtracted = target - nums[i]
            if subtracted in mapofvals:
                return [i, mapofvals[subtracted]]
            mapofvals[nums[i]] = i

        return [0,0]