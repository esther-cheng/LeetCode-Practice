class Solution(object):
    def isAnagram(self, s, t):
        dictionary = dict()

        if len(s) != len(t):
            return False

        for val1 in s:
            if val1 not in dictionary:
                dictionary.update({val1 : 1})
            else:
                dictionary.update({val1 : dictionary.get(val1)+1})
        
        for val2 in t:
            if val2 not in dictionary or dictionary.get(val2) == 0:
                return False
            else:
                dictionary.update({val2 : dictionary.get(val2) - 1})

        return True
