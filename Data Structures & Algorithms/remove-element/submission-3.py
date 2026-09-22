class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1  # reduce the size of the valid array
            else:
                l += 1  # move forward if the curr element is valid        
        return l    