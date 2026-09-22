class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = curr_area = 0

        while l < r:
            if heights[l] < heights[r]:
                curr_area = heights[l] * (r - l)
                max_area = max(max_area, curr_area)
                l += 1
            elif heights[l] > heights[r]:
                curr_area = heights[r] * (r - l)
                max_area = max(max_area, curr_area)
                r -= 1
            elif heights[l] == heights[r]:
                curr_area = heights[r] * (r - l)
                max_area = max(max_area, curr_area)
                r -= 1
        
        return max_area