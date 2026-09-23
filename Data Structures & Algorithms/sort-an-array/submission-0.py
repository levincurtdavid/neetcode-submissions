class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        temp = [0] * len(nums)

        def mergeSort(l, r):
            if l >= r:
                return
            
            m = (l + r) // 2

            mergeSort(l, m)
            mergeSort(m + 1, r)

            if nums[m] <= nums[m + 1]:
                return
            
            temp[l: r + 1] = nums[l: r + 1]

            i, j, k = l, m + 1, l

            while i <= m and j <= r:
                if temp[i] <= temp[j]:
                    nums[k] = temp[i]
                    i += 1
                else:
                    nums[k] = temp[j]
                    j += 1
                k += 1
            
            while i <= m:
                nums[k] = temp[i]
                i += 1
                k += 1
            
        mergeSort(0, len(nums) - 1)
        return nums