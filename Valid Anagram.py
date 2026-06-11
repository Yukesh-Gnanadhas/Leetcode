class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      # by sorting
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        return s == t
        
