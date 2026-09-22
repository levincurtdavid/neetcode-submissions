class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = postfix = 0

        for i in range(len(nums)):
            prefix = sum(nums[:i])
            postfix = sum(nums[i + 1:])
            if prefix == postfix:
                return i
        
        return -1