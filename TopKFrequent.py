class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using hashmap
        freq={}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        return sorted(freq, key = freq.get,reverse = True)[:k]
