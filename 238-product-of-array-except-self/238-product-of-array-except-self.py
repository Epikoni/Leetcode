class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [1 for _ in range (size)]
        
        left = 1
        for i in range(size):
            ans[i]*=left
            left*=nums[i]
        
        right =1
        for i in range(size-1,-1,-1):
            ans[i]*=right
            right*=nums[i]
        return ans