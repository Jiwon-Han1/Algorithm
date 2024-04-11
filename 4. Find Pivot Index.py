class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot_idx = 0

        while True:
            if len(nums) <= 1:
                break
            else:
                if sum(nums[0:pivot_idx]) != sum(nums[pivot_idx+1:len(nums)]):
                    pivot_idx = pivot_idx + 1
                else:
                    break 
            if pivot_idx == len(nums):
                pivot_idx = -1
                break     
        return pivot_idx
