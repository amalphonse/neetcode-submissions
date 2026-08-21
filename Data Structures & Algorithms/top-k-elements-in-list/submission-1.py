from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        counts=Counter(nums)
        
        sorted_pairs=sorted(counts.items(),key=lambda x: -x[1])
        return [key for key, pair in sorted_pairs[:k] ]