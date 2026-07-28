class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,high=0,len(nums)-1
        
        while low<=high:
            mid=(high+low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                mid+=1
                high-=1
            else:
                mid-=1
                low+=1
        return -1
