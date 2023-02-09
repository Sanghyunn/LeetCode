class Solution(object):
    def rotate(self, nums, k):
        k %= len(nums)
        
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
    def reverse(self, nums, start, end):
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1
            
            
    def swap(self, nums, first, second):
        temp = nums[first]
        nums[first] = nums[second]
        nums[second] = temp
        