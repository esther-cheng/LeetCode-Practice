class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ret = 0
        l = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            ret = max(ret, r-l + 1)

        return ret
            
            

