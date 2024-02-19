class Solution(object):
    def topKFrequent(self, nums, k):
        amts = {}
        arrAmts = [[] for i in range(len(nums) + 1)]
        ret = []

        for x in nums:
            amts[x] = amts.get(x, 0) + 1 #hashmap increments for the amt of a number
        
        for x in amts.keys():
            arrAmts[amts[x]].append(x)
    
        for i in range(len(arrAmts) - 1, 0, -1):
            for n in arrAmts[i]:
                ret.append(n)

                if len(ret) == k:
                    return ret

        
        