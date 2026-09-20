class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count, temp = 0, 0

        for n in nums:
            if n == 1:
                temp += 1
                max_count = max(max_count, temp)
            else:
                temp = 0
        
        return max_count

