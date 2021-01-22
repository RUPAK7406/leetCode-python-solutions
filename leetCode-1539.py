class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
         missingIntegers = []
        
         for i in range(1, 2001):
            if(i not in arr):
                missingIntegers.append(i)        
        
         return missingIntegers[k-1]
    
        