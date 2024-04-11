class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot_idx = 0
        sum_left = 0
        sum_right = sum(nums)

        while True:
            if len(nums) <= 1:
                break
            else:
                val = nums[pivot_idx]
                sum_right = sum_right - val
                if sum_left != sum_right:
                    pivot_idx = pivot_idx + 1
                    sum_left = sum_left + val
                else:
                    break 
            if pivot_idx == len(nums):
                pivot_idx = -1
                break     
        return pivot_idx
