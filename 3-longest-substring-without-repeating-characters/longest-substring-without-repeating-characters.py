class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visitedSet = set ()
        left = 0
        result = 0
        n = len(s)
        for right in range(n):
            while s[right] in visitedSet:
                visitedSet.remove(s[left])
                left += 1   
            visitedSet.add(s[right])      
            result = max(result, right - left + 1) 
        return result      