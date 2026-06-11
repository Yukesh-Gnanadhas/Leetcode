class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      # by sorting
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        return s == t
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using sorted method
        return sorted(s) == sorted(t)
   
