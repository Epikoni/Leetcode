class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            sum+=nums[i]
        cur_sum = 0
        for i in range(len(nums)):
            if(cur_sum*2 + nums[i] == sum):
                return i
            cur_sum+=nums[i]
        return -1