## Possible solution
1. get multi of all nums[i]
2. ans[i] = multi/nums[i] 
`
def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [1 for _ in range (size)]
        
        mult = 1
        for i in range(size):
            mult*=nums[i]
        
        for i in range(size):
            if nums[i]!=0:
                ans[i]=int(mult/nums[i])
            else:
                ans[i]=mult
        return ans
`
>Not work because nums[i] could be 0, mult = 0, ans got wrong
