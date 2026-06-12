class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #using hashmap
        seen={}
        for char in nums:
            seen[char] = seen.get(char, 0) + 1
            if seen[char]>1:
                return True
        return False
