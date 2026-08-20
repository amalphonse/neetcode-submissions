from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        
        for i in range(len(strs)):
            s="".join(sorted(strs[i]))
            result[s].append(strs[i])
            
        
        return list(result.values())
        