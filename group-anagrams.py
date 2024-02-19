class Solution(object):
    def groupAnagrams(self, strs):        
        anagrams = defaultdict(list)

        for num in strs:
            count = [0] * 26 # makes enough spaces to count alphabetically

            for letter in num:
                count[ord(letter) - ord("a")] +=1
            
            anagrams[tuple(count)].append(num)

        return anagrams.values()
        
        
