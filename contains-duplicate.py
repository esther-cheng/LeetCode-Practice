class Solution(object):
    def containsDuplicate(self, nums):
        repeats = set()

        for x in nums:
            if x not in repeats:
                repeats.add(x)
            else:
                return True

        return False
        